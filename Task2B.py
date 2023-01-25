from floodsystem import *
stations = build_station_list()
#print(stations)
update_water_levels(stations)
print(stations_level_over_threshold(stations, 0.8))