import requests
import os 
from termcolor import cprint

try:
    os.system("clear")
finally:
    os.system("cls")

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

while True:
    querry = input(">>> ")
    if len(querry) == 0:
        pass
    else:
        link  = f"http://thefury.pythonanywhere.com/fury?command={querry}"
        response = requests.get(link)
        response = response.text

        if "<!doctype html>" in response:
            re = response.split("<--",maxsplit=1)
            response = re[0]
        
            
        
        def web_opener(url):
            cprint(url,'cyan')
            try:
                os.system("termux-open-url " + url)
            except:
                pass

        def speak(text):
            if " <> " in text:
                text = str(text).split("<>")
                for reply in text:
                    cprint(reply,'red')
                    try:
                        os.system("termux-tts-speak "+ reply)
                    except:
                        pass
            else:
                cprint(text,'red')
                try:
                        os.system("termux-tts-engines "+ text)
                except:
                        pass

        if " <link> " in response:
            command = response.split("<link>",maxsplit=1)
            speak(command[0])
    #        try:
            links = command[1].split(",")

            for link in links:
                web_opener(link)
        else:
            
            speak(response)
