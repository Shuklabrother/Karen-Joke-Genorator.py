from androidhelper import sl4a
import pyjokes
import time

droid=sl4a.Android()

def speak(text):
       droid.ttsSpeak(text)

while True:
     speak(pyjokes.get_joke()) 
     time.sleep(10)