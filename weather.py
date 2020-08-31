import requests
from datetime import datetime
import pprint
import os
import time

secret_key = '85479ac044a523c7f202390713eb0461'


def current_weather(city):
    req_weather = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={secret_key}&units=metric"
    answer = {'feels_like': 0,  'temp': 0, 'sunset': 0, 'description': 0}
    resp = requests.get(req_weather)
    data = resp.json()
    if resp.status_code == 404:
        return
    answer['feels_like'] = data['main']['feels_like']
    answer['temp'] = data['main']['temp']
    time = data['sys']['sunset']
    answer['sunset'] = datetime.fromtimestamp(time).strftime("%H:%M:%S")
    answer['description'] = data['weather'][0]['description']
    return answer


def translate(data_text):

    alphabet_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    b = data_text
    b = b.lower()
    if b[0] in alphabet_rus:
        req = f"https://api.mymemory.translated.net/get?q={b}&langpair=ru|en"
    else:
        req = f"https://api.mymemory.translated.net/get?q={b}&langpair=en|ru"
    resp = requests.get(req)
    s1mple = resp.json()
    data = s1mple["responseData"]["translatedText"]
    return data


def weather_five_days(city):
    req_weather = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={secret_key}&units=metric'
    resp = requests.get(req_weather)
    data = resp.json()
    pprint.pprint(resp.json())



while True:
    a = input('Chto perevesti: ')

    print('Perevod:', translate(a))
    time.sleep(5)

    os.system('cls')
