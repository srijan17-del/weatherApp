import json

import requests
import pyttsx3


city = input("Enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=951f02f6313b4af6881152321230909&q={city}"
r = requests.get(url)
# print(r.text)
wdisc = json.loads(r.text)
print(wdisc["current"]["temp_c"])
w = wdisc["current"]["temp_c"]

engine = pyttsx3.init()
engine.say(f"The temperature of {city} is {w} degree celsius")
engine.runAndWait()

