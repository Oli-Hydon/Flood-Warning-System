from floodsystem import *
import datetime
risk_stations = build_station_list()
update_water_levels(risk_stations)

risk_stations = stations_highest_rel_level(risk_stations,5)
#date, level = fetch_measure_levels(risk_stations[0].measure_id,datetime.timedelta(days=10))
for i in risk_stations:
    date, level = fetch_measure_levels(i.measure_id,datetime.timedelta(days=10))
    plot_water_levels(i,date,level)
