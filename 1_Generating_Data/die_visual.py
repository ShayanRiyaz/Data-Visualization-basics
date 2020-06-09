from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


# Create a D6
die_1 = Die()
die_2 = Die(10)

num_times = 50_000
# Make some rolls, and store results in a list.
results = []
for roll_num in range(num_times):
 
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
    
# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
    
# Visualize the result.
x_values = list(range(2,max_result + 1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title' : 'Results','dtick':1}
y_axis_config = {'title' : 'Frequency fo Result'}

my_layout = Layout(title = f'Results of rolling two D6 and D10 dice {num_times} times',
                   xaxis = x_axis_config,
                   yaxis = y_axis_config)

offline.plot({'data'  : data,
              'layout': my_layout},filename = 'Assets/d6_d10.html')
                 
