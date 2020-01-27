from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Create lists to hold data
time_series = []
value_a_series = []
value_b_series = []

# This function is called periodically from FuncAnimation
def animate(i):

    # Add some data
    time_series.append(datetime.now())
    value_a_series.append(randint(0,10))

    # Clear the axis
    ax.clear()

    # Label the axis
    plt.title('An animated graph')
    plt.xlabel('Time')
    plt.ylabel('value_a')

    # Plot the data
    ax.plot(time_series, value_a_series, label='value_a_series')

    # Add a legend
    plt.legend()

    # Auto format the date
    fig.autofmt_xdate()


# Call the animation function every 1000ms
ani = animation.FuncAnimation(fig,
                              animate,
                              interval=1000)

# Show the plot
plt.show()