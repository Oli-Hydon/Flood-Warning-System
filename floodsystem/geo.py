# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
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