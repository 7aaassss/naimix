import requests



def predict(dob, lat, lon, tz):
    url = "https://api.vedicastroapi.com/v3-json/dashas/maha-dasha-predictions"
    dob_parts = dob.split("-")
    dob_reformatted = "/".join(dob_parts[::-1])

    params = {
        "dob": dob_reformatted,
        "tob": "12:00",
        "lat": lat,
        "lon": lon,
        "tz": tz,
        "api_key": "8663e1a4-5e18-51a8-8e03-33aee6a34ffe",
        "lang": "en"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        dashas = data["response"]["dashas"]
        plan = []
        pred = []
        for dasha in dashas:
            pred.append(dasha['prediction'])
            plan.append(dasha['planet_in_zodiac'])
        return pred, plan
    else:
        return "Некорректный ответ от API.", None

