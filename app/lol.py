import requests

url = "https://api.vedicastroapi.com/v3-json/dashas/maha-dasha-predictions"

def predict():
    params = {
        "dob": "14/03/2004",      # Дата рождения
        "tob": "13:00",            # Время рождения
        "lat": "61.7620",          # Широта Петрозаводска
        "lon": "34.3490",          # Долгота Петрозаводска
        "tz": "3",                 # Часовой пояс (UTC+3)
        "api_key": "cd30f913-9c2a-5da0-93ed-c33b5c777d0b",
        "lang": "en"               # Язык ответа
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return(response.json())
    else:
        return(f"Ошибка: {response.status_code}")






