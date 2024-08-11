# include necessary libraries
from django.urls import path

from scraperapi.views import EventListenerList, EventListenerDetail


urlpatterns = [
    path('<str:email>', EventListenerList.as_view()),
    path('<int:pk>', EventListenerDetail.as_view())
]