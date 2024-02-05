import requests

API_KEY = "7cc813f152116cb974a24d671691cf51"


def geocode(city, state, country):
    api_call = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=5&appid={API_KEY}"
    res = requests.get(api_call)
    return {"lon": res.json()[0]["lon"], "lat": res.json()[0]["lat"]}


def call_weather(lat, lon):
    api_call = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    res = requests.get(api_call)
    return res.json()


def main():
    default_country = "FI"
    default_state = "Finland"
    city = input("Minkä paikkakunnan sään haluat tietää?: ")

    loc = geocode(city, default_state, default_country)
    weather_call = call_weather(loc["lat"], loc["lon"])
    print(weather_call)
    weather = weather_call["weather"][0]
    # As Kelvin starts at absolute zero (-273.15C), we must offset the value.
    temp = weather_call["main"]["temp"] - 273.15
    print(weather)

    print(f"Paikkakunnan {city} säätila on:")
    print(f"{weather['main']}: {weather['description']}\nLämpötila: {'{:.2f}'.format(temp)} C")


main()
