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
