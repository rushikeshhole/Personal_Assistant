import os
import pyttsx3  #ofline mode text to speech translation

def tts(text):
    engine=pyttsx3.init()  
    voices = engine.getProperty('voices')  #to change the voice
    for voice in voices:
    	engine.setProperty('voice', voice.id)
    rate = engine.getProperty('rate')   #changing the voice rate or speak rate
    engine.setProperty('rate', rate)  #same    
    engine.say(text) 
    engine.runAndWait()

    
    





    
    