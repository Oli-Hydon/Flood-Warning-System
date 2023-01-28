from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from datetime import timedelta
stations = build_station_list()

time_delta = timedelta(days=2)
get_highest_stations = stations_highest_rel_level(stations, 6)

levels_for_each_station = [ [fetch_measure_levels(station.measure_id,time_delta),station] for station in get_highest_stations]
for data in levels_for_each_station:
    
    station = data[1]
    print(station)
    dates = data[0][0]
    levels = data[0][1]
    if len(dates)>10:
        plot_water_level_with_fit(station,dates,levels,4)

