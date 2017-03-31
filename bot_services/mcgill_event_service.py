import _datetime
from bot_mcgill.models import McgillEvent

class McgillEventService:
    def listAllDeadlines(self):
        academicEvents = McgillEvent.objects.filter(event_type='event_academic')
        eventsDict = {}
        i = 1
        deadlines = "Deadlines: \n\n"
        for event in academicEvents:
            dateString = _datetime.datetime.strftime(event.event_date, "%b %d %Y %H:%M:%S:%Z")
            deadlines += event.event_name + ", " + dateString + ". \n\n"
        return deadlines

    def get_event_in_major(self, major):
        majorEvents = McgillEvent.objects.filter(related_majors=major);
        if not majorEvents:
            return "There are no events in your major - " + major.name
        else:
            major_events = "Major events: \n\n"
            for event in majorEvents:
                dateString = _datetime.datetime.strftime(event.event_date, "%b %d %Y %H:%M:%S:%Z")
                major_events += event.event_name + ", " + dateString + ". \n\n"
            return major_events
