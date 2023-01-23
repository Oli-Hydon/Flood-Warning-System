from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


center = (52.2053, 0.1218)

radius = 10

stations = build_station_list()

stations_within_r = stations_within_radius(stations, center, radius) 

station_names_within_r = []
for i in stations_within_r: station_names_within_r.append(i.name)

station_names_within_r.sort()

print(station_names_within_r)