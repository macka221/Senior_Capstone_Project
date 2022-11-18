import requests
import json

from app.api.api_services.buildings import building, room
api_key = "ee97b4002e4cb219307255cb2643835a"

def calculateEnergyCostBuildingPerDay(building, long, lat):
    cost = 0
    for room in building.rooms:
        cost += calculateCostPerDay(room, long, lat, building.energy_cost)
    return cost

def calculateEnergyCostBuildingPerWeekForcast(building, long, lat):
    cost = 0
    days = getInitialTempWeekForcast(long, lat)
    CostPerDay = {}
    for day in days:
        costPerDay[day] = 0
        for room in building.rooms:
            costPerDay[day] += calculateCostPerDay(room, initial_temp, building.energy_cost)

    return CostPerDay

def calculateCostPerDay(room, long, lat, cost):
    return getCostPerHr(room, long, lat, cost) * 24

def calculateCostPerDay(room, initial_temp, cost):
    return getCostPerHr(room, initial_temp, cost) * 24

def calculateCostPerHr(room, long, lat, cost):
    power_used = getPowerUsed(room, long, lat)
    return power_used * 0.00029307 * cost

def calculateCostPerHr(room, initial_temp):
    power_used = getPowerUsed(room, initial_temp)
    return power_used * 0.00029307 * cost

def getPowerUsed(room, long, lat):
    initial_temp = getInitialTemp(long, lat)
    temp_change = room.desired_temp - initial_temp
    CFM = room.length * room.width * room.height * 60
    return 1.08 *CFM * temp_change

def getPowerUsed(room, initial_temp):
    temp_change = room.desired_temp - initial_temp
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

def getInitialTempWeekForcast(long, lat):
    weather_params = {"lat": lat,
                      "lon": long,
                      "cnt": 7,
                      "appid": api_key}

    weather_resp = requests.get(url="https://api.openweathermap.org/data/2.5/forecast/daily",
                                params=weather_params)

    print(weather_resp)
    weather_data = weather_resp.json()
    print(json.dumps(weather_data, indent=4))

    days = {}

    for day in weather_data['list']:
        days[day['dt']] = day['temp']['day']

    return days