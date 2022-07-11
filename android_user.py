from termcolor import cprint
import json
import requests
import os
from speak import say
from web_browse import web_opener


try:
    os.system("clear")
except:
    os.system("cls")
    
passcode = ["007","e@A$x788z339"]

cprint(    '''
                                   @              
                           .     .  @@(.           
                   (@#*. .  ,// #  .@@@%            
           .(                   &@@@@@@/    .     
       .(               ,&@@@@@@@@@@@@@@&        
       /*             (@@@@@@@@@@@@@@@@@@@@. .     
       @.           . @@ ,&@@@@@@@@@@@@@@@@@@@%..   
   %     .  &#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
   .,     .(@@@@@@@, ,.  @@@@@@@@@@@&&@&@@@@@*.@/*
   @/        &@@##     ..@@@@@@@&@@@@@@@@@@@@@*.@.
   ,,     *    ../  .....@&@@@@@@@@@@@@@@@@@@@%.. 
   @                .  .@@*,..@@@@@@@@@@@@@@@(@. 
   .,.%.            ,@@@@@.,....,@@@.@@@@@@@@@@ @  
       (              @&&......*&@*%@@@@@@@@@@&.   
       (,                ....,.,.@@@@@@@,@@@#@    
           .@          ......,...*@@@@@@@(@@&.,     
               @/      ......*&(*((,&@@% @@,        
                       ...  ...,@@//.  @           
                           ./@(     ,*             

    '''
,"green")
cprint("<--ENTER-PASSWORD-->","red")
i = input("$ --> ")
if i in passcode:
    while True:
        querry = input(">>> ")
        if len(querry) == 0:
            pass
        else:
            try:
                link  = f"https://thefury.pythonanywhere.com/fury?command={querry}"
                response = requests.get(link)
                status = response.status_code
                response = response.text
                if status == 500:
                    print("<--SERVER-ERROR-->")
                elif status == 200:
                    response = json.loads(response)
                    response = response["response"]
                    for every_reply  in response:
                        reply = every_reply[0]
                        text = reply[0]["text"]
                        if "link" in reply[0]:
                            link = reply[0]["link"]
                            for every_link in link:
                                #print(every_link)
                                web_opener(every_link)
                        say(text)
            except:
                print("<--CAN-NOT-CONNECT-TO-SERVER-->")
