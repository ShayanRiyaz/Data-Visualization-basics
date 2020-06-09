from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from datetime import datetime
import csv


num_rows = 10_000

# Explore the structure of the data
filename = 'data/world_fires_7_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
                  
    # Lists
    dates, brightnesses = [], []
    lats, lons = [], []
    hover_texts = []
    row_num = 0
    
    for row in reader:
        date = datetime.strptime(row[5], '%Y-%m-%d')  
        brightness = float(row[2])
        label = f"{date.strftime('%m/%d/%y')} - {brightness}"                         

        lats.append(row[0])
        lons.append(row[1])
        
        brightnesses.append(brightness)
        dates.append(date)
        hover_texts.append(label)

        row_num +=1
        if row_num == num_rows:
            break


    # Map the earthquakes.
    #data = [Scattergeo(lon=lons,lat=lats)]
    data = [{
        'type' : 'scattergeo',
        'lon'  : lons,
        'lat'  : lats,
        'text' : hover_texts,
        'marker' : {
            'size' : [brightness/50 for brightness in brightnesses],
            'color' : brightnesses,
            'colorscale': 'YlOrRd',
            'reversescale': True,
            'colorbar' : {'title' : 'Magnitude'},
        },
    }]
    my_layout = Layout(title = 'Global Fire Activity' )

    fig = {'data'   : data,
           'layout' : my_layout}
    offline.plot(fig,filename = 'Assets/global_fires.html')