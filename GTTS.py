from gtts import gTTS
import os
mytext= "Heloo"
language=  'en'
myobj=gTTS(text=mytext,lang=language,slow=False)
myobj.save("er.m4a")
os.system("er.m4a")
