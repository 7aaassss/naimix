import requests
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz


def get_coordinates(city_name):
    api_key = "9ad4b1ad5536e0ffb874d2cdf1752d20"
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            latitude = data[0]['lat']
            longitude = data[0]['lon']
            tz = get_timezone(latitude, longitude)
            return latitude, longitude, tz
        else:
            print("Город не найден.")
            return None, None, None
    else:
        print("Ошибка:", response.status_code, response.text)
        return None, None, None


def get_timezone(lat, lon):
    tf = TimezoneFinder()
    timezone_name = tf.timezone_at(lat=lat, lng=lon)
    if timezone_name:
        timezone = pytz.timezone(timezone_name)
        now = datetime.now()
        utc_offset = timezone.utcoffset(now).total_seconds() / 3600  # Смещение в часах
        return utc_offset
    else:
        print("Не удалось определить таймзону.")
        return None

