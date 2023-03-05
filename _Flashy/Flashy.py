import time
from multiprocessing import Process
from data import Data
from ui import FlashyUi
from pixela import increment_todays_pixel

LANG_FROM = 'en'
LANG_TO = 'ru'

data = Data(lang_from=LANG_FROM, lang_to=LANG_TO)
increment_todays_pixel()

# if __name__ == '__main__':
ui_processing = Process(target=FlashyUi(data))
ui_processing.start()
