from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = 'http://www.googleapis.com/auth/calendar'

#  CREDS .json file created on Google Cloud Platform, stored as config vars
#  on Heroku.
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPES)


#  CAL: Resource construct for interacting with the Google Calendar API
CAL = build('calendar', 'v3', credentials=CREDS)

#  CAL_ID: The ID of the specific calendar on Google Calendar
CAL_ID = 'l3pgnrii459d7a696a9pb0fcco@group.calendar.google.com'
GMT_OFF = '+02:00'

#  Get the current year and time
year = datetime.date.today().year
now = datetime.datetime.utcnow().isoformat() + GMT_OFF

def insrt_apt(cal, c_id, evnt):
    """
    Inserts a new event to the Google Calendar, from the user input.
    @param cal(resource): The calendar being called
    @param c_id(str): Google Calendar ID
    @param evnt(dict): Event inserted into calendar
    """

    cal.events().insert(  # pylint: disable=maybe-no-member
        calendarId=c_id,
        sendNotifications=True, body=evnt
    ).execute()

def main():
    event = {
        'summary': 'Google I/O 2015',
        'location': '800 Howard St., San Francisco, CA 94103',
        'description': 'A chance to hear more about Google\'s developer products.',
        'start': {
            'dateTime': '2021-11-06T09:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': '2021-11-06T10:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=2'
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    # pylint: disable=maybe-no-member
    insrt_apt(CAL, CAL_ID, event)


if __name__ == '__main__':
    main()
