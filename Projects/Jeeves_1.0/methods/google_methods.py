import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import google.generativeai as genai
from googleapiclient.discovery import build
from google.cloud import texttospeech
import datetime
from dateutil.parser import isoparse
from methods.logs_handler import *

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))

os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly',
          'https://www.googleapis.com/auth/tasks.readonly',
          'https://www.googleapis.com/auth/cloud-platform']


def get_credentials():
    creds = None
    token_path = os.path.join(MODULE_DIR, 'token.json')
    credentials_path = os.path.join(MODULE_DIR, 'credentials_desktop.json')
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                logging.error(f"Error refreshing token: {e}")
                creds = None
        if not creds or not creds.valid:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    return creds


def get_events_for_tomorrow():
    credentials = get_credentials()
    service = build('calendar', 'v3', credentials=credentials)

    now = datetime.datetime.utcnow()
    tomorrow_start = (now + datetime.timedelta(days=1)).replace(hour=4, minute=0, second=0, microsecond=0)
    tomorrow_end = (now + datetime.timedelta(days=2)).replace(hour=0, minute=0, second=0, microsecond=0)

    calendar_list = service.calendarList().list().execute()
    result = ['\nCalendar Events']
    for calendar in calendar_list['items']:
        calendar_id = calendar['id']
        events_result = service.events().list(
            calendarId=calendar_id,
            timeMin=tomorrow_start.isoformat() + 'Z',
            timeMax=tomorrow_end.isoformat() + 'Z',
            singleEvents=True,
            orderBy='startTime'
        ).execute()

        events = events_result.get('items', [])
        if events:
            result.append(f"Calendar: {calendar['summary']}")
            for i, event in enumerate(events, 1):
                start = event['start'].get('dateTime', event['start'].get('date'))
                end = event['end'].get('dateTime', event['end'].get('date'))
                start_dt = isoparse(start)
                end_dt = isoparse(end)
                duration = end_dt - start_dt
                hours, remainder = divmod(duration.seconds, 3600)
                minutes = remainder // 60
                duration_str = f"{hours}h{minutes:02d}min"
                description = event.get('summary', 'No description')
                if 'shift' in description:
                    description = 'Утренняя смена в Olympic Broadcasting Services'
                result.append(
                    f"{i}. Start: {start_dt.strftime('%H:%M')}, Duration: {duration_str}, Description: {description}")
        # # if we want to add info about calendars without events
        # else:
        #     result.append(f"\nCalendar: {calendar['summary']}")
        #     result.append("No events for tomorrow")
    if len(result) == 1:
        result.append("No events for tomorrow")
    return '\n'.join(result)


def get_tasks_for_tomorrow():
    credentials = get_credentials()
    service = build('tasks', 'v1', credentials=credentials)

    now = datetime.datetime.utcnow()
    tomorrow_start = (now + datetime.timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0,
                                                                tzinfo=datetime.timezone.utc)
    tomorrow_end = (now + datetime.timedelta(days=2)).replace(hour=0, minute=0, second=0, microsecond=0,
                                                              tzinfo=datetime.timezone.utc)

    task_lists = service.tasklists().list().execute()
    result = []
    for task_list in task_lists['items']:
        task_list_id = task_list['id']
        tasks_result = service.tasks().list(
            tasklist=task_list_id,
            showCompleted=False
        ).execute()

        tasks = tasks_result.get('items', [])
        if tasks:
            result.append(f"\n\nTask List: {task_list['title']}")
            for i, task in enumerate(tasks, 1):
                due = task.get('due', None)
                start = task.get('start', None)
                description = task.get('title', 'No description')

                if due:
                    due_dt = isoparse(due).astimezone(datetime.timezone.utc)
                    if tomorrow_start <= due_dt < tomorrow_end:
                        result.append(f"- {description}")
                elif start:
                    start_dt = isoparse(start).astimezone(datetime.timezone.utc)
                    if tomorrow_start <= start_dt < tomorrow_end:
                        result.append(f"- {description}")
                # # if we want to add tasks without due date
                # else:
                #     result.append(f"{i}. No Date, Description: {description}")
    if len(result) == 1:
        result.append("No tasks for tomorrow")
    return '\n'.join(result)


def query_google_genai(api_key, message):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(message)
    query = response.to_dict()['candidates'][0]['content']['parts'][0]['text']
    return query


def gen_mp3_with_google_text_to_speech(text):
    client = texttospeech.TextToSpeechClient(credentials=get_credentials())
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(language_code="en-IN", name='en-IN-Neural2-B')
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )
    return response.audio_content

