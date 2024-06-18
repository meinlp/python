import os.path
import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials_desktop.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    now = datetime.datetime.utcnow()
    tomorrow = (now + datetime.timedelta(days=1)).isoformat() + 'Z'  # 'Z' indicates UTC time
    now = now.isoformat() + 'Z'

    print('Getting the upcoming events for tomorrow')
    page_token = None
    while True:
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        for calendar_list_entry in calendar_list['items']:
            print('\nEvents for Calendar:', calendar_list_entry['summary'])
            events_result = service.events().list(
                calendarId=calendar_list_entry['id'],
                timeMin=now,
                timeMax=tomorrow,
                singleEvents=True,
                orderBy='startTime').execute()
            events = events_result.get('items', [])

            if not events:
                print('No upcoming events found.')
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])

        page_token = calendar_list.get('nextPageToken')
        if not page_token:
            break


if __name__ == '__main__':
    main()
