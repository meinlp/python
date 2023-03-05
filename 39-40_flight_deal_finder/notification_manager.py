from dotenv import load_dotenv
import os
import requests


# This class is responsible for sending notifications with the deal flight details.

class NotificationManager:
    def __init__(self):
        load_dotenv()
        self.bot_token = os.getenv('BOT_TOKEN')
        self.my_chat_id = os.getenv('MY_USER_ID')

    def send_message(self, bot_message: str):
        send_text = 'https://api.telegram.org/bot' + \
                    self.bot_token + '/sendMessage?chat_id=' + \
                    self.my_chat_id + '&parse_mode=Markdown&text=' + \
                    bot_message
        response = requests.get(send_text)
        return response.json()
