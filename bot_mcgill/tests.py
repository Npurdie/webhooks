from django.test import TestCase
from bot_mcgill.models import McgillEvent
from django.utils import timezone
from django.core import exceptions

# Create your tests here.

class McgillEventTestCase(TestCase):
    def testEventLinkValidator(self):
        invalidEventLink = "xd"
        event_name = "test"
        event_date = timezone.now()
        self.assertRaises(exceptions.FieldDoesNotExist,self.createAMcgillEvent(event_name,event_date,timezone.now()))

    def createAMcgillEvent(self, event_name, event_date, event_link):
        return McgillEvent(event_name=event_name, event_date=event_date, event_link=event_link)