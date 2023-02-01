from floodsystem import build_station_list, update_water_levels, stations_level_over_threshold
stations = build_station_list()
#print(stations)

update_water_levels(stations)
print(stations_level_over_threshold(stations, 0.8))