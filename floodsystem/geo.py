# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine
def stations_by_distance(stations,p) -> list:
    """
    Used to sort stations by distance from a coordiante p returns (Station,Distance) as the list items
    """
   

    unsorted_list=[]

    for i in stations:
        distance = haversine(p,i.coord)
        unsorted_list.append((i,distance))

    sorted_stations = sorted_by_key(unsorted_list,1)

    return sorted_stations

def stations_within_radius(stations, centre, r):
    """
    Used to list the stations within a cirtain radius r from a center
    """
    sorted_stations = stations_by_distance(stations,centre)

    stations_within_r = []
    for i in sorted_stations:
        if i[1] <= r:
            stations_within_r.append(i[0])
    
    return stations_within_r

def rivers_with_station(stations):
    """
    Returns a list of rivers with a station on them with no repeat rivers in the list
    """
    river_stations_list = []
    for i in stations:
        if type(i.river) == type(""):
            river_stations_list.append(i.river)
    river_stations_set = set(river_stations_list)
    return river_stations_set

def stations_by_river(stations):
    """
    Returns a dictionary with rivers as the key and the items are a list of stations that are upon that river
    """
    list_of_rivers = rivers_with_station(stations)
    stations_by_river_dict = {}
    for river in list_of_rivers:
        stations_on_river = []
        for station in stations:
            if station.river == river:
                stations_on_river.append(station)
        stations_by_river_dict.update({river:stations_on_river})
    return stations_by_river_dict

def rivers_by_station_number(stations, N):
    '''
    return N rivers with the largest number of stations, in a list of tuples, with their names and the number of staions on them
    '''
    result = []
    dic_of_rivers = stations_by_river(stations)
    #print(dic_of_rivers)
    list_of_rivers_names = list(dic_of_rivers.keys())
    list_of_rivers = []
    for i in list_of_rivers_names:
        #print(dic_of_rivers[i])
        list_of_rivers.append([i,len(dic_of_rivers[i])])
    #print(list_of_rivers)
    list_of_rivers.sort(key = lambda x :  x[1], reverse= True)
    #print(list_of_rivers)
    while(N < len(list_of_rivers)-1 and list_of_rivers[N+1][1] == list_of_rivers[N][1]):
        N += 1
    for i in range(0,len(list_of_rivers)):
        list_of_rivers = tuple(list_of_rivers[i])
    return list_of_rivers[0:N+1]
    
    
