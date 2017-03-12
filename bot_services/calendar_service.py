from __future__ import print_function
from oauth2client import tools
import urllib.parse as parser
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
    # summary = 'McBot%20Event',
    # location = '800%20Howard%20St.,%20San%20Francisco,%20CA%2094103',
    # description = 'A%20chance%20to%20hear%20more%20about%20Google\'s%20developer%20products.',
    # dates = '20170310T000000Z%2F20170310T010000Z&',
    # attendees = [
    #                 {'email': 'lpage@example.com'},
    #                 {'email': 'sbrin@example.com'},
    #             ],
    # reminders = ''
        #need to figure out how the API wants time to be written
    def create_event_client(self, name, description, dates = '20170310T000000Z/20170310T010000Z', location = '800 Howard St., San Francisco, CA 94103'):
        params =  '&text=' + parser.quote_plus(name) +'&dates=' + parser.quote_plus(dates) +'&details=' + parser.quote_plus(description) +'&location=' + parser.quote_plus(location)
        return 'http://www.google.com/calendar/event?action=TEMPLATE' + params