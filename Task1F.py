import floodsystem.stationdata
import floodsystem.station
from floodsystem.station import MonitoringStation
stations = floodsystem.stationdata.build_station_list()
floodsystem.stationdata.update_water_levels(stations)
print(floodsystem.station.inconsistent_typical_range_stations(stations))
