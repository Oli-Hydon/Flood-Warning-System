from floodsystem.geo import *
from floodsystem.stationdata import build_station_list
from random import randint
def test_stations_by_distance():
    #first test to see if the function works reliably without error
    stations = build_station_list()[:500]
    for station in stations:
        closest_station = stations_by_distance(stations,station.coord)[0][0]
       
        assert station.coord == closest_station.coord #check that the closest station is the correct one

    #next test for accuracy with known data

    data = stations_by_distance(stations,(48.622920,61.553804))
    #find the station calculated maually for

    for i in data:
        if i[0].station_id =="http://environment.data.gov.uk/flood-monitoring/id/stations/1029TH":
            assert round(i[1]-4371) == 0 #check distance correct
            break
    #check edge case
    closest_station = stations_by_distance([],(50,50))


def test_stations_within_raduis():
    #check to see if function works 
    #this test also checks accuracy
    lat = randint(-90000,90000)/1000
    long = randint(-90000,90000)/1000
    p = (lat,long)
    stations = build_station_list()[:500]
    for station in stations:

        station_distance = stations_by_distance([station],p)[0][1] +0.01
        stations_in = stations_within_radius(stations,p,station_distance)[-3:]
        assert station in stations_in


    
def test_rivers_with_station():
    stations = build_station_list()
    rivers = rivers_with_station(stations)

    assert "River Thames" in rivers

    #edge case
    rivers_with_station([])

def test_stations_by_river():
    stations = build_station_list()[:500]
    rivers = rivers_with_station(stations)
    for river in rivers:
        river_stations = stations_by_river(stations)
        river_stations = river_stations[river]
        for river_station in river_stations:
            assert river_station.river == river


def test_rivers_by_station_number():
    #test to see if the function works reliably
    stations = build_station_list()[:500]
    for i in range(len(stations)):
        data =rivers_by_station_number(stations,i)
        assert type(data[0][0])== str and type(data[0][1]) == int


    #test edge case

    rivers_by_station_number(stations,len(stations)+10)


