from django.core.management.base import BaseCommand
from bot_mcgill.models import McgillEvent
import json
import _datetime
import pytz
from bot_services.user_service import UserService, Question
from datetime import datetime
from fb_mcbot.models import Event

class Command(BaseCommand):

    help = 'Expires event objects which are out-of-date'

    def handle(self, *args, **options):
        print(Event.objects.filter(event_time__lt=datetime.now()).delete())