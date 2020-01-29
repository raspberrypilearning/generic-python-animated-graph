from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot()

# Create lists to hold data
time_series = []
value_a_series = []
value_b_series = []

# This function is called periodically from FuncAnimation

def generate_dummy_data():
    time = datetime.now()
    value_a = randint(-100, 100)
    value_b = randint(-10, 10)

    time_series.append(time)
    value_a_series.append(value_a)
    value_b_series.append(value_b)
    
def animate(i):

    # Add some data
    generate_dummy_data()
    
    # Clear the axis
    ax.clear()

    # Label the axis
    plt.title('An animated graph')
    plt.xlabel('Time')
    plt.ylabel('value_a')

    # Plot the data
    ax.plot(time_series, value_a_series, label='value_a_series')
    ax.plot(time_series, value_b_series, label='value_b_series')

    # Add a legend
    plt.legend()

    # Auto format the date
    fig.autofmt_xdate()
    print(i)

# Call the animation function every 1000ms
ani = animation.FuncAnimation(fig,
                              animate,
                              interval=1000)

#ani.save('/home/mjs/animate_graph.gif',writer='imagemagick', fps=10) 
#Show the plot
plt.show()

