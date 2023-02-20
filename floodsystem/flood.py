import datetime as dat
from numpy import poly1d
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.utils import sorted_by_key
from floodsystem.station import MonitoringStation

def stations_level_over_threshold(stations , tol):
    res = []
    for i in stations:
        if i.relative_water_level() == None:
            continue
        if i.relative_water_level() > tol:
            res.append((i.name,i.relative_water_level()))
    res = sorted_by_key(res, 1,True)
    return res
def stations_highest_rel_level(stations, N):
    stations.sort(key = lambda x : x.relative_water_level() if not x.relative_water_level() == None else float('-inf'),  reverse = True)
    return stations[:N]
def flood_warning(station : MonitoringStation):
    dt = 1
    percent = station.relative_water_level()
    if percent is None:
        return "data error"
    if(percent<0.5):
        return "low"
    elif percent<0.8:
        return "medium"
    else:
        try:
            dt = 1
            dates,levels = fetch_measure_levels(station.measure_id,dat.timedelta(days=dt))
            pf:poly1d= polyfit(dates, levels,3)[0]
            if(pf.deriv(1)((dates[0].timestamp()/86400))>=2):
                return "severe"
            else:
                return "high"
        except:
            return "data error"
