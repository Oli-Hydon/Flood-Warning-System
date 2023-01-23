from floodsystem.geo import rivers_with_station,stations_by_river
from floodsystem.stationdata import build_station_list

stations = build_station_list()

rivers = list(rivers_with_station(stations))
rivers.sort()
print("\n",len(rivers),"stations. First 10 -", rivers[:10],"\n")

river_list = ["River Aire", "River Cam", "River Thames"]

for river in river_list:
    stations_on_river =list(stations_by_river(stations)[river])
    for i in range(len(stations_on_river)):
        stations_on_river[i] = stations_on_river[i].name
    stations_on_river.sort()
    print(river,"-",stations_on_river,"\n")