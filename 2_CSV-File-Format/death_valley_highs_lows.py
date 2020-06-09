import csv

import matplotlib.pyplot as plt
from datetime import datetime
filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    
    for index,column_header in enumerate(header_row):
        print(index,column_header)
        
        
    # Get dates, high and low temperatures from this file.
    dates, highs,lows = [], [], []
    
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            
            
        # Plot the high temperatures.
    plt.style.use('seaborn')
    fig,ax = plt.subplots()
    ax.plot(dates,highs,c='red')
    ax.plot(dates,lows,c = 'blue')
    plt.fill_between(dates,highs,lows,facecolor = 'green', alpha = 0.2)
    
    
    # Format plot.
    plt.title("Daily High and Low Temperatures, 2018", fontsize = 24)
    plt.xlabel('',fontsize = 16)
    plt.ylabel("Temperatures (F)",fontsize = 16)
    fig.autofmt_xdate()
    plt.tick_params(axis = 'both',which = 'major', labelsize = 16)
    
    plt.show()