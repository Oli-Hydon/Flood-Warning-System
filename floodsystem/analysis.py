

import numpy as np
from floodsystem.datafetcher import fetch_measure_levels
from datetime import *
from floodsystem.station import MonitoringStation
import pytz

class data:
    def __init__(self, date :list[datetime], levels : list,p:int) -> None:
        if(date is None or len(date) == 0 or levels is None or len(date) != len(levels) or len(levels) == 0):
            print("data error")
        self.date = date
        self.levels = levels
        self.poly, self.offset= polyfit(date,levels,p)
        self.dt = date[-1]-date[0]
        assert(len(date) == len(levels))
    def __repr__(self):
        S = "date len: " + str(len(self.date))
        S += " level len: " + str(len(self.levels))
        S += " dt: " + str(self.dt)
        S+= " start: " +str(self.date[0])
        S+= " end: " +str(self.date[-1])
        S+= "\n polynomial fitting: \n" + str(self.poly)
        S+= "\n offset: " + str(self.offset)
        S+= " net above: " + str(self.net_above())
        return S
    def val(self, time: datetime):
        return self.poly(time.timestamp()/86400-self.offset)
    def net_above(self):
        try:
            sum = 0.0
            for i in range(len(self.date)-1):
                tempval = (self.levels[i] -self.val(self.date[i]))*(self.date[i+1]-self.date[i]).seconds/60.0
                #print (tempval)
                sum += (self.levels[i] -self.val(self.date[i]))*(self.date[i+1]-self.date[i]).seconds/60.0
            return sum/96.0
        except:
            print("data error")
            return 0
        
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
    
    print("start"+ str(flood_index_station.counter))
    flood_index_station.counter+=1
    dt = 3
    poly_deg = 1
    date,levels = fetch_measure_levels(station.measure_id,timedelta(days=dt))
    #print(date)
    #print(levels)
    #datetime.utcnow() -timedelta(days= 9)
    if(date is None or len(date) == 0 or levels is None or len(date) != len(levels)):
        print("data error")
        return 0 
    for i in range(len(date)):
        date[i]=date[i].replace(tzinfo=pytz.utc)
        pass
    #x = date[0]
    #print(x.tzinfo)
    past_data = []
    now = datetime.utcnow().replace(tzinfo=pytz.utc)
    for i in range(0,dt-1):
        temp_date = [x for x in date if x < (now - timedelta(days= i)) and x > (now - timedelta(days= i+1))]
        temp_level = [levels[o] for o in range(0,len(levels)) if date[o] in temp_date]
        past_data.append(data(temp_date,temp_level,poly_deg))
    for i in past_data:
        #print(i,"\n")
        #print(i.poly)
        pass
    polysum = np.poly1d(0)
    polycounter = 0
    for i in range(1,len(past_data)):
        polysum += past_data[i].poly
    #print(polysum)
    polysum = (polysum/[len(past_data)-1])[0]
    #print(polycounter)
    #print(polysum)
    #print()
    past_data[0].poly = polysum
    #print(len(past_data))
    #print(past_data[0].net_above())
    #print(past_data[0].date)
    #print(past_data[1].date)
    
    # for i in past_data:
    #     print("poly")
    #     print(i.poly)
    #     print("net")
    #     print(i.net_above())
    res = past_data[0].net_above()
    return res
flood_index_station.counter = 0