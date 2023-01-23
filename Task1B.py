from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

stations = build_station_list()

p=(52.2053, 0.1218)

closest_10_stations = stations_by_distance(stations,p)[:10]
furthest_10_stations = stations_by_distance(stations,p)[-10:]

def print_station_info(stations):
    print_list = []
    for i in stations:
        station_name = i[0].name
        station_town = i[0].town
        distance = i[1]
        print_list.append((station_name,station_town,distance))
    print(print_list)
print_station_info(closest_10_stations)
print_station_info(furthest_10_stations)