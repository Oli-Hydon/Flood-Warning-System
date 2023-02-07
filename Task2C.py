from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels
stations = build_station_list()
update_water_levels(stations)
res =stations_highest_rel_level(stations,10)
for i in res:
    print (i.name , '  ' , i.relative_water_level())