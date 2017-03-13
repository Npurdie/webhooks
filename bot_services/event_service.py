from bot_mcgill.models import McgillEvent
import json
import _datetime
import pytz
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