from floodsystem import *
stations = build_station_list()
update_water_levels(stations)
res =stations_highest_rel_level(stations,10)
for i in res:
    print (i.name , '  ' , i.relative_water_level())