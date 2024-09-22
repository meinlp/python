import os.path
import shutil
import random
import datetime
from methods.google_methods import (get_events_for_tomorrow, get_tasks_for_tomorrow, query_google_genai,
                                    gen_mp3_with_google_text_to_speech)
from methods.logs_handler import *
from dotenv import load_dotenv

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(CURRENT_DIR, '.env'))
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
remote_path = ('/Users/akaiumov/Library/CloudStorage/GoogleDrive-akaiumov@gmail.com/My '
               'Drive/tech/current_morning_alarm.mp3')


def main():
    logging.info(f'\n\n####### Creating an alarm for {tomorrow} #######')

    events = get_events_for_tomorrow()
    tasks = get_tasks_for_tomorrow()
    logging.debug(f'current events and tasks: {events}\n{tasks}')

    categories = [
        'animals',
        'music',
        'tech',
        'culture',
        'sport',
    ]
    something_else = (f'Also tell me a fun fact about {random.choice(categories)}. Start it with an announcement to '
                      f'separate from task list')
    message = (('You are a personal assistant, speaking respectfully but friendly and using ‘you’. You do not use '
                'emojis. I will see this message only tomorrow, so act as if tomorrow has already arrived. Based on '
                'the list of events and tasks, tell me about the schedule for the day. Tasks are completed during '
                'work, not after. Here is the list of tasks and events:\n') + events + '\n' + tasks + '\n' +
               something_else)

    genai_response = query_google_genai(api_key=GOOGLE_API_KEY, message=message)
    logging.info(f'message to generate: {genai_response}')

    alarm = gen_mp3_with_google_text_to_speech(genai_response)
    temp_path = f'{CURRENT_DIR}/alarm_{tomorrow}.mp3'
    with open(temp_path, "wb") as out:
        out.write(alarm)
        logging.info(f'Audio content written to file {temp_path}')
    shutil.copy(temp_path, remote_path)
    logging.info(f'{temp_path} was saved to {remote_path}')


if __name__ == '__main__':
    main()
