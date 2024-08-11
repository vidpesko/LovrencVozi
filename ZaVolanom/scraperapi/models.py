from django.db import models

# from scraper.main import get_all_categories
from scraperapi.validators import validate_event_date


EVENT_TYPE_CHOICES = {
    "vse": "Vse",
    "teorija": "Teorija",
    "voznja": "Voznja"
}


class EventListener(models.Model):
    """When user creates new reminder / event listener, it will be stored with this model"""
    email = models.EmailField()
    event_type = models.CharField(choices=EVENT_TYPE_CHOICES, default="vse", max_length=15)
    # categories = models.
    # district = models.CharField()
    # location = models.CharField()
    current_date = models.DateTimeField(validators=[validate_event_date])

    def __str__(self):
        return self.email
