from floodsystem.plot import *
from floodsystem.stationdata import build_station_list
import datetime
import numpy as np
def test_plot_water_levels():
    station = build_station_list(use_cache=True)[0]
    list_of_dates = [datetime.datetime.now()-datetime.timedelta(days=i) for i in range(10) ]
    levels = [i for i in range(10)]
    plot_water_levels(station,list_of_dates,levels,False)

def test_plot_water_level_with_fit():
    station = build_station_list(use_cache=True)[0]

    list_of_dates = [datetime.datetime.now()-datetime.timedelta(days=i) for i in range(10) ]

    know_poly_coefficents = np.array([3,-8,5])
    known_poly1d = np.poly1d(know_poly_coefficents)
    levels = [known_poly1d(i) for i in range(5,15)]
    
    plot_water_level_with_fit(station,list_of_dates,levels,2,False)


