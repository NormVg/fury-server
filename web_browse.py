import os 
from termcolor import cprint

def web_opener(url):
    cprint(url,'cyan')
    try:
        os.system("termux-open-url " + url)
    except:
        print("<--CAN-NOT-OPEN-WEBPAGE-->")