from floodsystem.analysis import polyfit
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np
def plot_water_levels(station, dates, levels):
    dates = np.array(dates)
    levels = np.array(levels)
  
    plt.plot(dates, levels)
# Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name+' relative water level')
# Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):

    poly_data, offset = polyfit(dates,levels,p)
    
    x1 = np.linspace(dates[0].timestamp()/86400, dates[-1].timestamp()/86400, len(levels))
    #print(x1)
    plt.plot(dates, poly_data(x1 - offset))
    plt.plot(dates,np.full(len(levels),station.typical_range[0]))
    plt.plot(dates,np.full(len(levels),station.typical_range[1]))

    plot_water_levels(station,dates,levels)

