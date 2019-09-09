#using sphinx
import speech_recognition as sr  
  
def stt():
     # obtain audio from the microphone  
     r = sr.Recognizer()  
     with sr.Microphone() as source:  
         print("Say something.....!")  
         audio = r.listen(source)  
         
    # recognize speech using Sphinx  
     try:
        wikiin=r.recognize_google(audio)
        #print(r.recognize_google(audio))
        return(wikiin)
         
     except sr.UnknownValueError:  
        print("Sphinx could not understand audio")  
     except sr.RequestError as e:  
        print("Sphinx error; {0}".format(e))  
stt()         

      
 
     #sppech to text input

