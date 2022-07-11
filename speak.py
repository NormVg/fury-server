import os 
from gtts import gTTS
from termcolor import cprint

def say(text):
    cprint(text,"red")
    speak=gTTS(text,lang="en")
    speak.save("tts.mp3")
    os.system(f"termux-media-player play tts.mp3")
    os.remove("tts.mp3")
    
