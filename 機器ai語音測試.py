import speech_recognition

def listenTo():
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    return r.recognize_google(audio, language='zh-TW')



from gtts import gTTS
from pygame import mixer
import tempfile

mixer.init()

def speak(sentence):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence, lang='zh')
        tts.save("{}.mp3".format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()
import requests
def getWeather():
    res = requests.get('https://works.ioa.tw/weather/api/weathers/1.json')
    temp = res.json()['felt_air_temp']
    
    return '現在溫度是 {} 度'.format(temp)

qa = {
    '早安': '你也早安',
    '你好帥': '你也好帥',
    '我的老天鵝': '九四八七九四狂',
    '誰是最帥的': '當然是你呀',
    '請告訴我天氣': getWeather()}

speak(qa.get(listenTo(), '我現在聽不懂你的問題, 但當我變聰明以後, 我就會回答了'))