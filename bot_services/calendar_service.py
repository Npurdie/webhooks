from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
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
CLIENT_ID = '362386413877-7c39vktq1du448tnti5d5fr7qs8jfa3d.apps.googleusercontent.com'
CLIENT_SECRET = 'YUM0eM5AOAJZfCrLEL6YHMp2'
APP_NAME_SHORT = 'McBot'

class CalendarService:
    http = ""
    service = ""
    credentials = ""

    #prompts for appplication authentication on object creation!
    def __init__(self):
        x = 0
#         self.create_event_client()
#        self.get_credentials()
#        self.http = self.credentials.authorize(httplib2.Http())
#        self.service = discovery.build('calendar', 'v3', http=self.http)

#prompts the server side, not the client side
#    def get_credentials(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
"""        """
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
            #auth_uri = flow.step1_get_authorize_url()
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        self.credentials = credentials
        return credentials

#creates the link to pass to the user for them to authenticate the app with google
    def get_credentials_client(self):
        flow = OAuth2WebServerFlow(client_id=CLIENT_ID,
                           client_secret=CLIENT_SECRET,
                           scope=SCOPES,
                           redirect_uri='https://localhost/')
        auth_uri = flow.step1_get_authorize_url()
        print(auth_uri)
        return auth_uri
"""
        #need to figure out how the API wants time to be writtern
    def create_event_client(self, summary = 'McBot%20Event',
        location = '800%20Howard%20St.,%20San%20Francisco,%20CA%2094103',
        description = 'A%20chance%20to%20hear%20more%20about%20Google\'s%20developer%20products.',
        dates = '20170310T000000Z%2F20170310T010000Z&',
        attendees = [
                {'email': 'lpage@example.com'},
                {'email': 'sbrin@example.com'},
            ],
        reminders = ''):
        result =  'http://www.google.com/calendar/event?action=TEMPLATE' + '&text=' + summary +'&dates=' + dates +'&details=' + description +'&location=' + location
        print(result)
        return result
"""
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




def main():
    myCalendar = CalendarService()
#    myCalendar.create_event()


if __name__ == '__main__':
    main()

    """
