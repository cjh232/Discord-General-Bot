import requests
import secrets

api_key = secrets.WEATHER_API

base_url = "http://api.openweathermap.org/data/2.5/weather?q="


def get_weather(city_name, tags):
    complete_url = base_url + city_name + "&appid=" + api_key + "&units=imperial"

    response = requests.get(complete_url)

    all_tags = 'a' in tags
    empty_tags = len(tags) == 0

    x = response.json()

    if x["cod"] != "404":

        y = x["main"]

        current_temp = y["temp"]

        feels_like = y["feels_like"]

        current_pressure = y["pressure"]

        current_humidity = y["humidity"]

        z = x["weather"]

        weather_desc = z[0]["description"]

        wind = x["wind"]
        wind_speed = wind["speed"]

        res = {
            "city": city_name,
        }

        temp_logo = '🥶' if current_temp < 40 else '🌞'

        if 'd' in tags or all_tags or empty_tags:
            res["desc"] = weather_desc.capitalize()
        if 't' in tags or all_tags or empty_tags:
            res["Current Temp:"] = f"🌡️ {current_temp} °F"
        if 'f' in tags or all_tags or empty_tags:
            res["Feels Like:"] = f"{temp_logo}  {feels_like} °F"
        if 'h' in tags or all_tags or empty_tags:
            res["Humidity:"] = f"💦  {current_humidity}%"
        if 'p' in tags or all_tags:
            res["Pressure:"] = f"🔽  {current_pressure} hPa"
        if 'w' in tags or all_tags or empty_tags:
            res["Wind Speed:"] = f"💨  {wind_speed} mph"

        return res
    else:
        return {"city": "Error", "desc": "City was not found."}
