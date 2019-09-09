import wikipedia
from offline_TTS import *

def wiki(input):
    a=wikipedia.summary(input,sentences=3)
    mytext= a
    print(a)
    
    tts(a)
    
    

        


