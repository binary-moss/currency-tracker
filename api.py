import requests

def fetch_rates(): # Работа с сайтом ЦБ
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    data = response.json()
    return data['Valute'] # Возвращаем словарь из всех валют
