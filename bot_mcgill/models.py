from django.db import models
from fb_mcbot.models import Major

# Create your models here.

class McgillEvent(models.Model):
    EVENT_TYPES = (  # enum of options of event types
        ('event_academic', 'Academic Deadlines'),
        ('event_facebook', 'Facebook Event'),
        ('event_misc', 'Misc'),
    )
    event_name = models.CharField(max_length=70)
    event_date = models.DateTimeField()
    event_link = models.URLField(blank=True)
    event_type = models.CharField(max_length=70, choices=EVENT_TYPES, default='event_academic')
    related_majors = models.ManyToManyField(Major);
    def __str__(self):
        return ("%s" % (self.event_name))

    def set_event_name(self, event_name):
        self.event_name = event_name
        self.save()

    def set_event_date(self, event_date):
        self.event_date = event_date
        self.save()

    def set_event_link(self, event_link):
        self.event_link = event_link
        self.save()