from floodsystem.flood import *
from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.station import MonitoringStation
from random import randint
def test_stations_level_over_threshold():
    stations = build_station_list()
    stations_level_over_threshold(stations,1)   #checks the function can handle none type data as all none types before update
    update_water_levels(stations)
    for i in range (100):   ##try 100 different tolerances
        test_tol = randint(0,10000)/10000 #gives a random level between 0 and 1

        stations_level_over_threshold(stations,test_tol)    ##checks function runs 

        assert(len(stations_level_over_threshold(stations,test_tol)) > 1)   #checks function reutrns atleast some stations



def test_stations_highest_rel_level():
    stations = build_station_list()
    returned_stations=stations_highest_rel_level(stations,len(stations))
    for returned_station in returned_stations:
        assert(type(returned_station)==(MonitoringStation))    #Checks the function reutrns the correct data type and chekcs that it handles missing data
test_stations_level_over_threshold()