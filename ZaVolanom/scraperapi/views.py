from rest_framework import generics

from scraperapi.models import EventListener
from scraperapi.serializers import EventListenerSerializer


class EventListenerList(generics.ListCreateAPIView):
    """
    List all events or create new one
    """
    queryset = EventListener.objects.all()
    serializer_class = EventListenerSerializer

    def get_queryset(self):
        """
        Filter queryset with email
        """
        email = self.kwargs["email"]
        return EventListener.objects.filter(email=email)


class EventListenerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventListener.objects.all()
    serializer_class = EventListenerSerializer
