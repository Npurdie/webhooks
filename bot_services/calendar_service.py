from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime
try:
    import argparse
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None

# very much copied from the Google Calendar API Python Quickstart tutorial

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.readonly','https://www.googleapis.com/auth/plus.login'
CLIENT_SECRET_FILE = 'calendar_auth.json'
APPLICATION_NAME = 'ECSE428 - McBot'

class CalendarService:
    http = ""
    service = ""
    credentials = ""

    #prompts for appplication authentication on object creation!
    def __init__(self):
        self.get_credentials()
        self.http = self.credentials.authorize(httplib2.Http())
        self.service = discovery.build('calendar', 'v3', http=self.http)

    def get_credentials(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'calendar-python-quickstart.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        self.credentials = credentials

    def create_event(self):
        event = self.load_event()
        event = self.service.events().insert(calendarId='primary', body=event).execute()
        return 'Event created'

    def load_event(self, summary = 'McBot Event',
        location = '800 Howard St., San Francisco, CA 94103',
        description = 'A chance to hear more about Google\'s developer products.',
        startTime = '2017-03-28T09:00:00-07:00',
        endTime = '2017-03-28T17:00:00-07:00',
        timeZone = 'America/Los_Angeles',
        attendees = [
                {'email': 'lpage@example.com'},
                {'email': 'sbrin@example.com'},
            ],
        reminders = ''):
        event = {
            'summary': summary,
            'location': location,
            'description': description,
            'start': {
                'dateTime': startTime,
                'timeZone': timeZone,
            },
            'end': {
                'dateTime': endTime,
                'timeZone': timeZone,
            },
            'recurrence': [
                 'RRULE:FREQ=DAILY;COUNT=2'
            ],
            'attendees': attendees,
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
        return event


#Sample code for creating a calendar object and creating the default event
#(load create_event() with arguments to populate it)

def main():
    myCalendar = CalendarService()
    myCalendar.create_event()


if __name__ == '__main__':
    main()
