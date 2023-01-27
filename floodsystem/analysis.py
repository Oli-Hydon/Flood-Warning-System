

import numpy as np
import matplotlib.pyplot as plt


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
    print(x)
    polynomial_coefficents = np.polyfit(x-x[-1],levels,p)
    
    poly_data=np.poly1d(polynomial_coefficents)

    return (poly_data,x[-1])

    
