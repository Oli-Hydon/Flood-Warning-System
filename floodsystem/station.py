# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None
        self.floodindex = -1000




    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    def typical_range_consistent(self):
        # determining whether the range of the object is valid, return false for invalid range
        if(self.typical_range is None):
            return False
        if(self.typical_range[0]>self.typical_range[1]):
            return False
        return True

    def relative_water_level(self):
        # return the relative water level of the station, none for invalid input. 0 for lowest, 1 for highest
        if not self.typical_range_consistent() or self.latest_level is None:
            return None
        else:
            return (self.latest_level - self.typical_range[0])/(self.typical_range[1]-self.typical_range[0])
        pass
    
def inconsistent_typical_range_stations(stations):
    #creating a list of names of stations that have invalid typical range
    res = []
    for i in stations:
        if (not i.typical_range_consistent()):
            res.append(i.name)
            #print(i.typical_range)
    res.sort()
    return res