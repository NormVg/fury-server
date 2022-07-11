import os ,time
from gtts import gTTS
from termcolor import cprint

def say(text):
    speak=gTTS(text,lang="en")
    speak.save("tts.mp3")
    os.system(f"termux-media-player play tts.mp3")
    cprint(text,"cyan")
    time.sleep(.5)
    os.remove("tts.mp3")
    
