from django.core.management.base import BaseCommand

class Command(BaseCommand):

    help = 'Expires event objects which are out-of-date'

    def handle(self, *args, **options):
        #print(Event.objects.filter(date__lt=datetime.datetime.now()).delete())
        print('Hello World')
