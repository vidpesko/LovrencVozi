import re

import requests
from bs4 import BeautifulSoup


base_url = "https://e-uprava.gov.si/si/javne-evidence/prosti-termini/content/singleton.html"
test_url = "https://e-uprava.gov.si/si/javne-evidence/prosti-termini/content/singleton.html?type=-&cat=4&cat=2&cat=3&cat=1&izpitniCenter=17&lokacija=-1&offset=400&sentinel_type=ok&sentinel_status=ok&is_ajax=1"
# query_params = {
    
# } 

response = requests.get(test_url)
print("Got response")
html = response.content

soup = BeautifulSoup(html, "lxml")

all_displayed_events = soup.find_all("div", class_="js_dogodekBox dogodek")

for event in all_displayed_events:
    # Event date
    event_date: str = event.find("div", class_="calendarBox")["aria-label"]

    event_content = event.find("div", class_="contentOpomnik")
    # Seats left
    seats_left_str: str = str(event_content.find("div", class_="lessImportant green").string)
    seats_left: int = int(re.findall(r"\d+", seats_left_str)[0])

    # Event title
    event_title: str = str(event_content.find("div", string=re.compile("Preverjanje")).string)

    # Event location
    event_location: str = "".join(list(event_content.find("div", class_="upperOpomnikDiv").stripped_strings))

    
