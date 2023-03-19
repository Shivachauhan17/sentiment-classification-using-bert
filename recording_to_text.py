import sounddevice as sd 
from scipy.io.wavfile import write
import numpy as np

freq = 44100
duration=10
print("speak")
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
sd.wait()

y = (np.iinfo(np.int32).max * (recording/np.abs(recording).max())).astype(np.int32)
write("recording0.wav", freq, y)

import speech_recognition as sr


r=sr.Recognizer()

with sr.AudioFile('recording0.wav') as source:
    audio_data = r.record(source)
    text=r.recognize_google(audio_data)
    print(text)