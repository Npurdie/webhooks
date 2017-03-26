from bot_mcgill.models import McgillEvent
import json
import _datetime
import pytz
import re
from bot_services.user_service import UserService, Question
from bot_services.communication_service import CommunicationService
from datetime import datetime
from dateutil.parser import parse
from fb_mcbot.models import Event

QUESTION_EVENT_NAME = 'EVENT_NAME'
QUESTION_EVENT_LOCATION = 'EVENT_LOCATION'
QUESTION_EVENT_DESCRIPTION = 'EVENT_DESCRIPTION'
QUESTION_EVENT_LINK = 'EVENT_LINK'
QUESTION_EVENT_DATE = 'EVENT_DATE'
QUESTION_EVENT_CONFIRMATION = 'EVENT_CONFIRMATION'
QUESTION_NOTHING = 'NOTHING'

class EventService:

    def listAllDeadlines(self):
        academicEvents = McgillEvent.objects.filter(event_type='event_academic')
        eventsDict = {}
        i = 1
        deadlines = "Deadlines: "
        for event in academicEvents:
            dateString = _datetime.datetime.strftime(event.event_date, "%b %d %Y %H:%M:%S:%Z")
            deadlines += event.event_name + ", " + dateString + ". "
        return deadlines

    def get_event_id_from_link(link):
        print(link)
        p = re.compile('\d+(?!=\d)')
        m = p.search(link)
        if not m:
            raise Exception('not valid link')
        return m.group(0)

    def create_new_event(conversation, link):
        ssociety = UserService.get_student_society(conversation.fbuser)
        eventId = EventService.get_event_id_from_link(link)
        if (eventId is None):
            raise
        try:
            event = CommunicationService.get_event_info(eventId)
        except Exception:
            raise
        event_info = event.json()
        new_event = Event()
        new_event.link = link
        new_event.creator = ssociety
        new_event.name = event_info['name']
        new_event.event_time = parse(event_info['end_time']).strftime('%Y-%m-%d %H:%M:%S')
        new_event.category = event_info['category']
        new_event.save()

    def get_most_recent_event(conversation):
        ssociety = UserService.get_student_society(conversation.fbuser)
        # recent_event = Event.objects.filter(creator = ssociety).order_by('creation_time')[0]
        recent_event = Event.objects.filter(creator = ssociety).latest('creation_time')
        return recent_event

    def initEvent(conversation, link):
        try:
            EventService.create_new_event(conversation, link)
            return "Event created"
        except Exception as e:
            return str(e)

    def get_events():
        now = datetime.now()
        events =  Event.objects.filter(event_time__gte = now)
        result = ""
        for e in events:
            result += "\n[" + e.name + "]: " + e.link
        return result
