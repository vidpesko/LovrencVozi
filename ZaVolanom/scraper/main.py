import re
import datetime
from uuid import uuid4
from typing import List

import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel, ValidationError, Field

import global_variables as gv

# try:
#     from graph_building import Neo4jDatabase, GTFS
# except:
#     from .graph_building import Neo4jDatabase, GTFS


class Event(BaseModel):
    id: str = Field(default_factory=lambda: uuid4().hex)
    # Starting date and time
    date: datetime.datetime  # Also includes starting time
    duration: int  # In minutes
    # Location
    district: str
    location: str
    full_location: str  # full_location is "district + location"

    seats_left: int
    title: str
    categories: List[str]


class FilterOption(BaseModel):
    value: str
    label: str


class Filter(BaseModel):
    input_name: str  # Name attribute of <input> tag
    group_name: str  # Which property it filters (e.g.: Kategorija, Območje,...) 
    options: List[FilterOption]


class Scraper:
    """Interface to e-uprava.gov website. This class is not only used for returning events, but also possible filters about location, categories,..."""
    def get_and_load_html(self, url: str) -> BeautifulSoup:
        """Get and load html into bs4

        Args:
            url (str): url

        Returns:
            BeautifulSoup: soup object
        """
        response = requests.get(url)
        html = response.content
        return BeautifulSoup(html, gv.SCRAPER_PARSER)

    def get_dropdown_options(self, select_html) -> List[FilterOption]:
        options = []
        for option in select_html.children:
            if option == "\n":
                continue

            value = option["value"]
            label = str(option.string).strip()
            
            option = FilterOption(
                value=value,
                label=label
            )
            options.append(option)
        return options

    def get_events(self, url: str) -> List[Event]:
        """Retrieve all events on page from url

        Args:
            url (str): url with all filters
        Returns:
            pydantic BaseModel
        """
        events = []

        soup = self.get_and_load_html(url)

        all_displayed_events = soup.find_all("div", class_="js_dogodekBox")
        for event in all_displayed_events:
            # Event date
            event_date: str = event.find("div", class_="calendarBox")["aria-label"].strip()

            event_content = event.find("div", class_="contentOpomnik")
            # Seats left
            seats_left_str: str = str(
                event_content.find("div", class_="lessImportant green").string
            )
            event_seats_left: int = int(re.findall(r"\d+", seats_left_str)[0])

            # Event title
            event_title: str = str(
                event_content.find("div", string=re.compile("Preverjanje")).string
            ).strip()

            # Event location
            event_location_list: list = list(event_content.find("div", class_="upperOpomnikDiv").stripped_strings)
            event_district: str = event_location_list[0]
            event_location: str = event_location_list[1]
            event_location = event_location.replace(",", "").strip()
            event_full_location: str = event_district + ", " + event_location

            # Categories
            categories_html = event_content.find_all("div")[-2].find_all("span")
            event_categories: list[str] = [str(c.string).strip() for c in categories_html]

            # Start time
            event_start_time_html = event_content.find_all("div")[-1]
            event_start_time: str = str(event_start_time_html.span.string).strip()

            # Event duration
            event_duration_raw = list(event_start_time_html.stripped_strings)[-1]
            event_duration: int = int(re.findall(r"\d+", event_duration_raw)[0])
            
            # Convert event date to datetime
            event_date += (" " + event_start_time)
            event_start_time_full = datetime.datetime.strptime(event_date, "%d. %m. %Y %H:%M")

            # Parse data into pydantic model
            try:
                event_model = Event(
                    date=event_start_time_full,
                    duration=event_duration,
                    district=event_district,
                    location=event_location,
                    full_location=event_full_location,
                    seats_left=event_seats_left,
                    title=event_title,
                    categories=event_categories
                )
                events.append(event_model)
            # If some data is not in right format
            except ValidationError as e:
                print("Error")

        return events

    def get_filters(self, url: str) -> List[Filter]:
        """Retrive all query filters

        Args:
            url (str): url
        Returns:
            List[Filter]: list of filters
        """
        filters = []

        soup = self.get_and_load_html(url)
        filters_container = soup.find("div", class_="blueBox noMargin js_filtriExtrasContainer")
        filters_groups = filters_container.find_all("fieldset")

        for group in filters_groups:
            # Which data this filter affects
            filter_group_name = group.find("legend").string

            # Check if it is location filter
            if filter_group_name == "Območje":
                # Get districts
                district_filter_html = group.find("select", id="izpitniCenter-ID")
                district_filter_input_name = district_filter_html["name"]
                
                district_filter = Filter(
                    input_name=district_filter_input_name,
                    group_name="Območje",
                    options=self.get_dropdown_options(district_filter_html)
                )

                # Get locations
                location_filter_html = filters_container.find("select", id="lokacija-ID")
                location_filter_input_name = location_filter_html["name"]
                
                location_filter = Filter(
                    input_name=location_filter_input_name,
                    group_name="Lokacija",
                    options=self.get_dropdown_options(location_filter_html)
                )

                filters.append(district_filter)
                filters.append(location_filter)
                continue

            options = []
            # Go through input and label field
            for filter_input in group.find_all("input"):
                input_name = filter_input["name"]
                input_value = filter_input["value"]

                # Get label
                input_id = filter_input["id"]
                label = str(group.find("label", {"for": input_id}).string).strip()

                option = FilterOption(
                    value=input_value,
                    label=label
                )
                options.append(option)

            filter_model = Filter(
                input_name=input_name,
                group_name=filter_group_name,
                options=options
            )
            filters.append(filter_model)

        return filters


s = Scraper()
filters = s.get_filters(gv.MAIN_PAGE_URL)
# print(filters)
