import os
from offline_TTS import *;
import wolframalpha
def wol(wolin):
    app_id ="XKL2T9-WWRT3Y69W3"
    client = wolframalpha.Client(app_id)
    my_input = wolin
    res = client.query(my_input)
    answer = next(res.results).text 
    print(answer)
    tts(answer)
    



