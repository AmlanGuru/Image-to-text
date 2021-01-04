import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
from PyDictionary import PyDictionary
import pyautogui
from PIL import Image
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

dict= PyDictionary()
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say('Hello there, how are you doing today')

def talk(text):

    engine.say('Listening now..')
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Rox' in command:
                command = command.replace('Rox','')
                print(command)
    except:
        pass
    return command

def run_Rox():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song + 'for you daddy')
        pywhatkit.playonyt(song)
        print('Playing it for you bey')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        talk('It is' + time)
        print(time)
    elif 'who is' in command:
        who= command.replace('who is','')
        info=wikipedia.summary(who,2)
        talk(info)
    elif 'search' in command:
        what = command.replace('search','')
        info2 = wikipedia.summary(what,2)
        talk(info2)
    elif 'what is' in command:
        what2 = command.replace('what is','')
        info3 = wikipedia.summary(what2,2)
        talk(info3)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)
    elif 'stop' in command:
        talk('Goodbye. Have a nice day')
        print('Switching off')
        sys.exit()
    elif 'read' in command:
        talk('Reading now')
        print('Reading')
        img  = Image.open("text_to_convert.png")
        output = pytesseract.image_to_string(img)
        talk(output)
    else:
        talk('Please speak again')

while True:
    run_Rox()
