from django.test import TestCase

from rest_framework.test import APIRequestFactory, APITestCase

from scraperapi.models import EventListener


class EventListenerTests(TestCase, APITestCase):
    def test_get_with_no_email():
        pass
