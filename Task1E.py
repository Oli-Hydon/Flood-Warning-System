import floodsystem.stationdata
import floodsystem.geo
stations = floodsystem.stationdata.build_station_list()
#print(stations[0])
#stations = floodsystem.geo.stations_by_river(stations)
#print(len(stations))
print(floodsystem.geo.rivers_by_station_number(stations,9))
