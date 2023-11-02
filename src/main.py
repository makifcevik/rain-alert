import requests

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "YOUR API KEY HERE"
city_lat = 41.008240
city_log = 28.978359

parameters = {
    "lat": city_lat,
    "lon": city_log,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
data = response.json()

data["hourly"] = data["hourly"][:12]
condition_codes = []
rainy = False
for i in range(len(data["hourly"])):
    condition_codes.append(data["hourly"][i]["weather"][0]["id"])  # extract weather ids
    if condition_codes[i] < 700:
        rainy = True

if rainy:
    print("Bring an umbrella...")
print(condition_codes)
