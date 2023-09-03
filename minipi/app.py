from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)

# 음성인식 관련 초기화
recognizer = sr.Recognizer()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start_recognition", methods=["POST"])
def start_recognition():
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ko-KR")
        return text
    except:
        return "음성을 인식하지 못했습니다."


if __name__ == "__main__":
    app.run(debug=True)
