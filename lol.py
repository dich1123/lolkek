import requests

resp = requests.get('http://rzhunemogu.ru/RandJSON.aspx?CType=1')

print(resp.text)
print(resp.json())

"""
requests - модуль, который позволяет отправлять запросы по http

requests.get() - отправить get запрос
requests.post(body={}) - отправить post запрос

______________________________
resp = requests.get('https://some-web.com') 
b = resp.text - в переменную b записать ответ на наш запрос в виде строки
c = resp.json() - в переменную с записать ответ на запрос в виде словаря
                  (обычно, только API(специальные ресурсы, которые просто
                  отдают информацию, а не html) возвращают словари)  
"""
