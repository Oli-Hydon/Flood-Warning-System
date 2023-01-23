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
    sorted_stations = stations_by_distance(stations,centre)

    stations_within_r = []
    for i in sorted_stations:
        if i[1] <= r:
            stations_within_r.append(i[0])
    
    return stations_within_r
