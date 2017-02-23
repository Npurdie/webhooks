from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

SCOPES = 'https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.readonly','https://www.googleapis.com/auth/plus.login'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'McBot - Google Calendar'

def get_credentials():
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
    return credentials

def create_event(service):
    event = load_event()
    event = service.events().insert(calendarId='primary', body=event).execute()
    print ('Event created')

def load_event(summary = 'Google I/O 2015',
    location = '800 Howard St., San Francisco, CA 94103',
    description = 'A chance to hear more about Google\'s developer products.',
    startTime = '2017-01-28T09:00:00-07:00',
    endTime = '2017-01-28T17:00:00-07:00',
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
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    create_event(service)


if __name__ == '__main__':
    main()
