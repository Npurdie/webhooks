from bot_mcgill.models import McgillEvent
import json
import _datetime
import pytz
from bot_services.user_service import UserService, Question
from datetime import datetime
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

    def create_new_event(conversation):
        ssociety = UserService.get_student_society(conversation.fbuser)
        new_event = Event()
        new_event.creator = ssociety
        new_event.save()

    def get_most_recent_event(conversation):
        ssociety = UserService.get_student_society(conversation.fbuser)
        # recent_event = Event.objects.filter(creator = ssociety).order_by('creation_time')[0]
        recent_event = Event.objects.filter(creator = ssociety).latest('creation_time')
        return recent_event

    def initEvent(conversation):
        EventService.create_new_event(conversation)
        conversation.set_conversation_question(Question.get_question_type(QUESTION_EVENT_NAME))
        return "please enter event name"

    def format_event_details(event):
        details = "\nEvent Details:" + "\n[Event Name]: " + event.name + "\n[Event Location]: " + event.location \
                + "\n[Event Description]: " + event.description + "\n[Event Date]: " + event.event_time  \
                + "\n[Event Link]: " + event.link
        print(details)
        return details

    def validate_date(d):
        try:
            datetime.strptime(d, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def confirm_event(event, msg):
        if (msg != 'y'):
            event.delete()
            return "event not saved"
        return "event saved"

    def processEvent(conversation, msg):
        event = EventService.get_most_recent_event(conversation)
        if (conversation.question == Question.get_question_type(QUESTION_EVENT_NAME)):
            event.name = msg
            event.save()
            conversation.set_conversation_question(Question.get_question_type(QUESTION_EVENT_LOCATION))
            return "please enter location"
        elif (conversation.question == Question.get_question_type(QUESTION_EVENT_LOCATION)):
            event.location = msg
            event.save()
            conversation.set_conversation_question(Question.get_question_type(QUESTION_EVENT_DESCRIPTION))
            return "please enter event description"
        elif (conversation.question == Question.get_question_type(QUESTION_EVENT_DESCRIPTION)):
            event.description = msg
            event.save()
            conversation.set_conversation_question(Question.get_question_type(QUESTION_EVENT_LINK))
            return "please enter event link"
        elif (conversation.question == Question.get_question_type(QUESTION_EVENT_LINK)):
            event.link = msg
            event.save()
            conversation.set_conversation_question(Question.get_question_type(QUESTION_EVENT_DATE))
            return "please enter event date in [yyyy-mm-dd] format"
        elif (conversation.question == Question.get_question_type(QUESTION_EVENT_DATE)):
            if (EventService.validate_date(msg)):
                event.event_time = msg
                event.save()
                conversation.set_conversation_question(Question.get_question_type(QUESTION_EVENT_CONFIRMATION))
                return EventService.format_event_details(event) + "\n\nPlease type [y] to save the event"
            else:
                return "please enter event date in [yyyy-mm-dd] format"
        elif (conversation.question == Question.get_question_type(QUESTION_EVENT_CONFIRMATION)):
            reply = EventService.confirm_event(event, msg)
            conversation.set_conversation_question(Question.get_question_type(QUESTION_NOTHING))
            return reply
