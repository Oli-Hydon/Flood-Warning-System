from floodsystem.analysis import *
import datetime as dt
import numpy as np

"""
Unit test for analysis module
"""


def test_polyfit():
    #start by testing quadratic fit
    #test for the quadratic 3x^2 - 8x +5
    # known points (0,5), (1,0), (1.667,0)

    dates = [dt.datetime(1970,1,2,17), dt.datetime(1970,1,2,1), dt.datetime(1970,1,1,1)]       ##x coordinates converted to days since 1970
    levels = [0,0,5]
    returned_poly =  polyfit(dates,levels,2)[0]
    
    know_poly_coefficents = np.array([3,-8,5])
    known_poly1d = np.poly1d(know_poly_coefficents)
    
    for i in range (2,100):
        assert( round(known_poly1d(i) - returned_poly(i)) == 0)
    


    #test offset_value
    #the previous values for the dates had an offset of 0 adding 5 days to all those dates should give an offset of 5
    for known_offset in range(1,100):
        for i in range(len(dates)):
            print(dates[i])
            dates[i] += dt.timedelta(days=1)    #adds a day to the offset each loop

        returned_offset = polyfit(dates,levels,2)[1]
        print(known_offset,returned_offset)
        assert round(returned_offset-(known_offset)) == 0     #tests if the offset returned by the polyfit function matches what it should be
    
test_polyfit()