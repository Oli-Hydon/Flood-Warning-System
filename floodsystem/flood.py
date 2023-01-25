import sys
from floodsystem import * 
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
