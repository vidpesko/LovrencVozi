from rest_framework import serializers

from scraperapi.validators import validate_event_date
from scraperapi.models import EVENT_TYPE_CHOICES, EventListener


# class EventListenerSerializer(serializers.Serializer):
#     """When user creates new reminder / event listener, it will be stored with EventListener model and parsed to JSON with this serializer"""
#     email = serializers.EmailField()
#     event_type = serializers.ChoiceField(
#         choices=EVENT_TYPE_CHOICES, default="vse"
#     )
#     # categories = models.
#     # district = models.CharField()
#     # location = models.CharField()
#     current_date = serializers.DateTimeField(validators=[validate_event_date])

#     def create(self, validated_data):
#         """
#         Create and return new EventListener instance, given the validated data
#         """
#         return EventListener.objects.create(**validated_data)

#     def update(self, instance: EventListener, validated_data):
#         """
#         Update and return an existing `EventListener` instance, given the validated data.
#         """
#         instance.email = validated_data.get("email", instance.email)
#         instance.event_type = validated_data.get("event-type", instance.event_type)
#         instance.current_date = validated_data.get("current-date", instance.current_date)
#         instance.save()
#         return instance

class EventListenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventListener
        fields = ["id", "email", "event_type", "current_date"]