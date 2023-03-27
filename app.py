from flask import Flask, render_template, request
import pickle 
import sounddevice as sd 
from scipy.io.wavfile import write
import numpy as np
import pandas as pd
import nltk
import speech_recognition as sr
import matplotlib.pyplot as plt

app=Flask(__name__)

def voice_to_text(duration):
    freq = 44100

    print("speak")
    recording = sd.rec(int(duration*60 * freq), samplerate=freq, channels=2)
    sd.wait()

    y = (np.iinfo(np.int32).max * (recording/np.abs(recording).max())).astype(np.int32)
    write("recording0.wav", freq, y)



    r=sr.Recognizer()

    with sr.AudioFile('recording0.wav') as source:
        audio_data = r.record(source)
        text=r.recognize_google(audio_data)
    
    all_text=[nltk.sent_tokenize(text)]
    return all_text

def text_to_plot(text):
    model=pickle.load(open('model.pkl','rb'))
    result=[]
    for i in text:
        res=model.predict([i])
        res=np.argmax(res[0])
        result.append(res)
        df=pd.DataFrame(result,columns=['result'])
        

@app.route('/',methods=['POST','GET'])
def hello():
    return render_template('index.html')
 
@app.route('/output',methods=['POST','GET'])
def voice_to_plot():
      
if __name__ =='__main__':
	app.debug = True
	app.run(debug = True,port=8000)