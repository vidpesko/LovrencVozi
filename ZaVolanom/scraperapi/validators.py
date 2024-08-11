# Model field validators
from django.utils import timezone
from django.core.exceptions import ValidationError


def validate_event_date(value):
    if value < timezone.now():
        raise ValidationError(
            "Izbrani datum za izpit je nepravilen."
        )