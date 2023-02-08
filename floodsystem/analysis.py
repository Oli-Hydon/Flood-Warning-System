

import numpy as np
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.station import MonitoringStation


def polyfit(dates, levels, p):
    """
    Given dates and water levels it fits them to a polynomial of order p and returns a numpy poly1d class as well as the amount of offset days since 1/1/1970
    """
    x = []
    for date in dates:
        epoch_time = date.timestamp()
        in_days =  epoch_time /86400
        x.append(in_days)
    x=np.array(x)
    polynomial_coefficents = np.polyfit(x-x[-1],levels,p)
    
    poly_data=np.poly1d(polynomial_coefficents)

    return (poly_data,x[-1]) 

def flood_index_station(station : MonitoringStation):
    date,levels = fetch_measure_levels(station.measure_id,datetime.timedelta(days=10))
    poly_data,offset = polyfit(date, levels,3)

def sum(poly_data:np.poly1d,dates:list,levels:list):
    sum = 0
    for i in range(len(dates)):
        
        if(dates):
            pass
