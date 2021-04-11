import os
from papago import Translator
import pyautogui as pya
from pynput.keyboard import Key, Listener
import pyperclip
import time
from window import Window
from langdetect import detect

CLIENT_ID = "********************"
CLIENT_SECRET = "********"
translator = Translator(CLIENT_ID, CLIENT_SECRET)
class Translate:
    def __init__(self):
        self.get_selected()
        self.decide_translate()
        self.display()  # we past the translated text, and the korean for naver dict access.

    def decide_translate(self):
        toTranslate = self.toTranslate
        lang = detect(toTranslate)  # Detect which language we want to translate
        if lang == 'ko':  # if korean, translate korean to english.
            self.translated = translator.translate(toTranslate, 'ko', 'en').text
            self.korean = toTranslate
        else:  # if english, translate english to korean
            self.translated = translator.translate(toTranslate, 'en', 'ko').text
            self.korean = self.translated

    def get_selected(self):
        pya.hotkey('ctrl', 'c')
        time.sleep(.01)  # ctrl-c is usually very fast but program may execute faster
        self.toTranslate = pyperclip.paste()

    def display(self):
        self.opened = True
        currentMouseX, currentMouseY = pya.position()
        self.window = Window(self.translated, currentMouseX - 5, currentMouseY - 100)
        self.window.run(self.korean)  # passing korean so that we can click and go to naver dict

def on_press(key):
    if key == Key.scroll_lock:
        Translate()

while True:
    with Listener(on_press=on_press) as listener:
        listener.join()


