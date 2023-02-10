
from floodsystem.analysis import *
from floodsystem.stationdata import *
import datetime as dt
from datetime import datetime
import numpy as np
import multiprocessing
from floodsystem.flood import stations_level_over_threshold

"""
Unit test for analysis module
"""


def test_polyfit():
    #start by testing quadratic fit
    #test for the quadratic 3x^2 - 8x +5
    # known points (0,5), (1,0), (1.667,0)
    from floodsystem.analysis import polyfit
    import datetime as dt
    from datetime import datetime
    import numpy as np
    from floodsystem.flood import stations_level_over_threshold
    dates = [datetime(1970,1,2,17), datetime(1970,1,2,1), datetime(1970,1,1,1)]       ##x coordinates converted to days since 1970
    levels = [0,0,5]
    returned_poly =  polyfit(dates,levels,2)[0]
    
    know_poly_coefficents = np.array([3,-8,5])
    known_poly1d = np.poly1d(know_poly_coefficents)
    
    for i in range (2,100):
        assert( round(known_poly1d(i) - returned_poly(i)) == 0)
    


    #test offset_value
    #the previous values for the dates had an offset of 0 adding 5 days to all those dates should give an offset of 5
    for known_offset in range(1,100):
        for i in range(len(dates)):
            print(dates[i])
            dates[i] += dt.timedelta(days=1)    #adds a day to the offset each loop

        returned_offset = polyfit(dates,levels,2)[1]
        print(known_offset,returned_offset)
        assert round(returned_offset-(known_offset)) == 0     #tests if the offset returned by the polyfit function matches what it should be
    
# def test_flood_index_station():
#     stations = build_station_list()
    
#     for station in stations:
#         if station.name == 'Cam':
#             station_cam = station
#             break
#     #print(station_cam)
    
#     for i in stations:
#         i.floodindex = flood_index_station(i)
#         if i.floodindex >0:
#             print(i)
#             print(i.floodindex)
        
#     stations.sort(key= lambda x: x.floodindex)
#     print(stations[:25]) 
#     #now = dt.datetime.utcnow()
#     #diff = timedelta(days=2)
#     # Start time for data
#     #start = now - diff
# def test_sum():
    
    # pass
#test_flood_index_station()

if __name__ ==  '__main__':
    test_polyfit()
    stations = build_station_list()
    update_water_levels(stations)
    stations = [i for i in stations if i.relative_water_level() is not None and i.relative_water_level()>0.8]
    print(len(stations))
    with multiprocessing.Pool(processes=15) as p:
        procs = p.map(flood_index_station, stations) 
    
    print("station count "+ str(len(stations)))
    for i in range(len(stations)):
        stations[i].floodindex = procs[i]
        #print(stations[i].name + str(stations[i].floodindex))
    stations.sort(key= lambda x: x.floodindex,reverse=True)
    for i in range(len(stations)):
        print(stations[i].name + str(stations[i].floodindex))