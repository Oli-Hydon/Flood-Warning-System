from floodsystem.flood import flood_warning
from floodsystem.stationdata import build_station_list, update_water_levels
stations = build_station_list()
update_water_levels(stations)
levels = [(x,flood_warning(x)) for x in stations]
levels.sort(key = lambda x : {"severe":4,"high" : 3,"medium":2,"low":1,"data error":0}[x[1]],reverse = True)
print(levels[:10])
