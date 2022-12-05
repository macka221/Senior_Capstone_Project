from energy import *
from buildings import building, room

newRoom = room(temp=294.81, length=5, width=4, height=3, max_occupancy=12,
                       room_number=1)
newRooms = []

for i in range(10):
    newRoom = room(temp=294.81, length=5, width=4, height=3, max_occupancy=12,
                   room_number=1)
    newRooms.append(newRoom)
newBuilding = building(address="water", rooms=newRooms, name="dansby",manager="brandon", consumption=1)

print(calculateEnergyCostBuildingPerWeekForcast(newBuilding, -84.4255, 33.7561))
