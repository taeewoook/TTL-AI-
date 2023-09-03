import speech_recognition as sr
import sys
import io

# -*- coding: euc-kr -*-
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

r = sr.Recognizer()

# 마이크
with sr.Microphone() as source:
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language="ko-KR")
    print("You Said: {}".format(text))
except:
    print("Sorry, could not recognize you voice.")
