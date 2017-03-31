from django.core.management.base import BaseCommand
from datetime import datetime
from fb_mcbot.models import Event

class Command(BaseCommand):

    help = 'Expires event objects which are out-of-date'

    def handle(self, *args, **options):
        print(Event.objects.filter(event_time__lt=datetime.now()).delete())