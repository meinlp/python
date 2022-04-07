import requests
import os
from dotenv import load_dotenv


def send_message_with_tg_bot(bot_message: str):
    load_dotenv()
    bot_token = os.getenv('BOT_TOKEN')
    my_chat_id = os.getenv('MY_USER_ID')
    send_text = 'https://api.telegram.org/bot' + \
                bot_token + '/sendMessage?chat_id=' + \
                my_chat_id + '&parse_mode=Markdown&text=' + \
                bot_message
    response = requests.get(send_text)
    return response.json()


send_message_with_tg_bot("San Francisco, April 6 (Reuters) - Toyota Motor (7203.T) unit Woven Planet has joined Tesla Inc (TSLA.O) in trying to advance self-driving technology without expensive sensors such as lidars.\r\nWoven \u2026 [+2468 chars]")