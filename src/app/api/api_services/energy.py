import requests
import json

api_key = "226093ea0eea721cf942b92091d1cabc"

def getCostPerDay(final_temp, zip, l, w, h, cost):
    return getCostPerHr(final_temp, zip, l, w, h, cost) * 24

def getCostPerHr(final_temp, zip, l, w, h, cost):
    power_used = getPowerUsed(final_temp, zip, l, w, h)
    return power_used * 0.00029307 * cost

def getPowerUsed(final_temp, zip, l, w, h):
    intial_temp = getInitialTemp(zip)
    temp_change = final_temp - intial_temp
    CFM = l * w * h * 60
    return 1.08 *CFM * temp_change

def getInitialTemp(zip):
    location_params = {
        "zip": zip,
        "apid": api_key
    }
    location_resp = requests.get(url="http://api.openweathermap.org/geo/1.0/zip",
                                 params=location_params)

    print(location_resp)

    location_data = location_resp.json()

    print(location_data)

    lon = location_data["lon"]
    lat = location_data["lat"]

    print("lon is ", lon)
    print('lat is', lat)

    weather_params = {"lat": lat,
                      "lon": lon,
                      "appid": api_key}

    weather_resp = requests.get(url="https://api.openweathermap.org/data/2.5/weather",
                                params=weather_params)

    print(weather_resp)
    weather_data = weather_resp.json()
    print(json.dumps(weather_data, indent=4))

    return weather_data["main"]["temp"]