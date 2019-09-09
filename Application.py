import os
import io
from offline_TTS import *
message="Hi..........What can i Help You" 

tts(message+os.getlogin())
for i in range(6):
    
    from offline_TTS import *;
    uti="Say Something"      #uti= user text input
    tts(uti+os.getlogin())                 #uti to the TTS
        
    from offspeech import *;
    sti=stt()
    
    #sti=input("Enter the search")
    print(sti)              #sti=speech text input   speech input givent to the sti variable

    from wiki import *;
    try:
         from wol import *
         wolout=wol(sti)
         tts(wolout)
            
    except:
        #tts("check your network connection")
        #print("Check your network connection")
        
         
        wikiout=wiki(sti)         #wikiout=wikipedia output
        tts(wikiout)
    
    
             
("Thank You")




    
    