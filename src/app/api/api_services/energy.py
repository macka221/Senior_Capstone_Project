import requests
import json

from app.api.api_services.buildings import building, room
api_key = "226093ea0eea721cf942b92091d1cabc"

def calculateEnergyCostBuildingPerDay(building, long, lat):
    cost = 0
    for room in building.rooms:
        cost += calculateCostPerDay(room, long, lat, building.energy_cost)
    return cost

def calculateCostPerDay(room, long, lat, cost):
    return getCostPerHr(room, long, lat, cost) * 24

def calculateCostPerHr(room, long, lat, cost):
    power_used = getPowerUsed(room, long, lat)
    return power_used * 0.00029307 * cost

def getPowerUsed(room, long, lat):
    intial_temp = getInitialTemp(long, lat)
    temp_change = room.desired_temp - intial_temp
    CFM = room.length * room.width * room.height * 60
    return 1.08 *CFM * temp_change

def getInitialTemp(long, lat):
    weather_params = {"lat": lat,
                      "lon": long,
                      "appid": api_key}

    weather_resp = requests.get(url="https://api.openweathermap.org/data/2.5/weather",
                                params=weather_params)

    print(weather_resp)
    weather_data = weather_resp.json()
    print(json.dumps(weather_data, indent=4))

    return weather_data["main"]["temp"]