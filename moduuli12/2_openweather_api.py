import requests
API_KEY = "7cc813f152116cb974a24d671691cf51"

def geocode(city, state, country):
  API_CALL = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=5&appid={API_KEY}"
  return requests.get(API_CALL)
  

def call_weather(lat, lon):
  API_CALL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"

def main():
  DEFAULT_COUNTRY = "FI"
  DEFAULT_STATE = "Finland"
  test_loc = geocode("Helsinki",DEFAULT_STATE,DEFAULT_COUNTRY)
  print(test_loc.json())
  
main()