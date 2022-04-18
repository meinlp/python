import pyttsx3
from gtts import gTTS
import os


def gtts_synth(message):
    filename = 'temp.mp3'

    synth = gTTS(text=message, lang='en', slow=False)
    synth.save(filename)

    os.system(f"mpg321 {filename}")
    os.remove(filename)


def pyttsx3_synth(message):
    pyttsx3_synthesizer = pyttsx3.init()
    # # tryin' out different voices
    # voices = pyttsx3_synthesizer.getProperty('voices')
    # for voice in voices:
    #     i = voice.languages
    #     if 'ru' in i[0].split('_'):
    #         print("\n\nVoice:")
    #         print("ID: %s" % voice.id)
    #         print("Name: %s" % voice.name)
    #         print("Age: %s" % voice.age)
    #         print("Gender: %s" % voice.gender)
    #         print("Languages Known: %s" % voice.languages)
    #         msg = f"Привет, синтезатор работает и на русском. Меня зовут {voice.name}, мне {voice.age} лет."
    #         pyttsx3_synthesizer.setProperty('voice', voice.id)
    #         pyttsx3_synthesizer.say(msg)
    #         pyttsx3_synthesizer.runAndWait()
    #         pyttsx3_synthesizer.stop()
    pyttsx3_synthesizer.setProperty('voice', 'com.apple.speech.synthesis.voice.karen')  # I fukken adore Karen
    pyttsx3_synthesizer.say(message)
    pyttsx3_synthesizer.runAndWait()
    pyttsx3_synthesizer.stop()


gtts_synth("hello, I'm a Google text to speech synthesizer, it's a test message")
pyttsx3_synth("hello, I'm pyTTSX3 text to speech synthesizer, my name is Karen, it's a test message")
