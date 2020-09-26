# -*- coding: utf-8 -*- 

import speech_recognition as sr

r = sr.Recognizer()
harvard = sr.AudioFile('C:/Users/lysyi/Desktop/audio convector/m.wav')
with harvard as source:
	audio = r.record(source,  duration=15)

text = r.recognize_google(audio, language="uk-UA")
open('C:/Users/lysyi/Desktop/audio convector/recognize_google.txt','w').write(text)
