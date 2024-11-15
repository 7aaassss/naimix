import requests
import json
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
import time

api_key = "8663e1a4-5e18-51a8-8e03-33aee6a34ffe"
dob = "14/03/2004"
tob = "12:00"
base_url = "https://api.vedicastroapi.com/v3-json/dashas/maha-dasha-predictions"

coordinates = [
    [51.509865, -0.118092],
    [48.856613, 2.352222],
    [31.233334, 30.033333],
    [55.755825, 37.617298],
    [25.276987, 55.296249],
    [23.810331, 90.412521],
    [51.169392, 71.449074],
    [13.756331, 100.501762],
    [1.352083, 103.819839],
    [35.689487, 139.691711],
    [-33.868820, 151.209290],
    [-9.443800, 159.949800],
    [-41.286640, 174.775570],
    [64.135484, -21.895411],
    [-54.801911, -68.302952],
    [-23.550520, -46.633308],
    [10.480594, -66.903603],
    [40.712776, -74.005974],
    [19.432608, -99.133209],
    [39.739235, -104.990250],
    [34.052235, -118.243683],
    [61.218056, -149.900284],
    [21.306944, -157.858337],
    [-9.000000, -140.000000],
    [0.000000, -180.000000]
]

months = [f"{str(m).zfill(2)}/03/2004" for m in range(1, 13)]

results = []

for lat, lon in coordinates:
    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lat=lat, lng=lon)
    if not timezone_str:
        print(f"Не удалось определить таймзону для координат ({lat}, {lon}). Пропускаем.")
        continue

    timezone = pytz.timezone(timezone_str)
    now = datetime.now()
    localized_now = timezone.localize(now)
    offset = localized_now.utcoffset().total_seconds() / 3600


    for month in months:
        params = {
            "dob": dob,
            "tob": tob,
            "lat": lat,
            "lon": lon,
            "tz": offset,
            "api_key": api_key,
            "lang": "en"
        }
        try:
            response = requests.get(base_url, params=params)

            if response.status_code == 200:
                data = response.json()
                dashas = data["response"]["dashas"]
                for dasha in dashas:
                    prediction = dasha["prediction"]
                    planet_in_zodiac = dasha["planet_in_zodiac"]
                    results.append({
                        "prediction": prediction,
                        "planet_in_zodiac": planet_in_zodiac
                    })
            else:
                print(f"Error for coordinates ({lat}, {lon}), month {month}: {response.status_code}")
        except Exception as e:
            break

# сохранение данных в файл
with open("predictions.json", "w") as file:
    json.dump(results, file, indent=4)

print("end")
