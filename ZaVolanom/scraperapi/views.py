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



# @api_view(["GET", "POST"])
# def listener_list(request):
#     """
#     List all event listeners, or create a new one
#     """
#     if request.method == "GET":
#         listeners = EventListener.objects.all()
#         serializer = EventListenerSerializer(listeners, many=True)
#         return Response(serializer.data, safe=False)
#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = EventListenerSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET", "PUT", "DELETE"])
# def listener_detail(request, pk):
#     """
#     Retrive, update or delete specific listener
#     """
#     try:
#         listener = EventListener.objects.get(pk=pk)
#     except EventListener.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = EventListenerSerializer(listener)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = EventListenerSerializer(listener,  data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         listener.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
