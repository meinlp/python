# from dict_converter import *
from data import Data
from ui import FlashyUi

LANG_FROM = 'en'
LANG_TO = 'ru'

data = Data(lang_from=LANG_FROM, lang_to=LANG_TO)
ui = FlashyUi(data)
