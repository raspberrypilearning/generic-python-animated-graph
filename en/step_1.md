Here's how you can animate a graph using `matplotlib` in Python. This can be used to live monitor sensor data, or data streamed to your computer over the internet.

![animated graph showing random data being plotted over time](images/animate_graph.gif)
--- task ---

You can install matplotlib using a package manager such as `apt` or `pip`.

```bash
sudo pip3 install matplotlib #using pip
sudo apt install python3-matplotlib #debian based linux
```

--- /task ---

--- task ---

Open a new Python file in your preferred IDE or text editor

--- /task ---

--- task ---

Now import the required modules. Note that the `datetime` and `random` modules are used to simulate a data source and are not required for live graphing.

```python
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
import matplotlib.animation as animation
```

--- /task ---

--- task ---

Now you can create figure and subplot objects. The figure is the actual graph while the subplot is the axis of the graph.

```python
fig = plt.figure()
ax = fig.add_subplot()
```

--- /task ---

--- task ---

Now create lists to hold the data. This will be dummy data in this example.

```python
time_series = []
value_a_series = []
value_b_series = []
```

--- /task ---

--- task ---

Now create a function to generate some dummy data, for use with the graph. In reality this would be a function to collect real data, maybe from a sensor.

```python
def generate_dummy_data():
    time = datetime.now()
    value_a = randint(-100, 100)
    value_b = randint(-10, 10)

    time_series.append(time)
    value_a_series.append(value_a)
    value_b_series.append(value_b)
```

--- /task ---

--- task ---

Next create a function to draw an animated graph.

```python
def animate(i):

    generate_dummy_data()
```

--- /task ---

--- task ---

As the axis of the graph can constantly change, they need to be cleared and redrawn each time new data has been added.

```python
    ax.clear()

    plt.title('An animated graph')
    plt.xlabel('Time')
    plt.ylabel('values')
```

--- /task ---

--- task ---

Now you can plot the contents of the list or lists of data. In this example two lines will be drawn.

```python
    ax.plot(time_series, value_a_series, label='value_a_series')
    ax.plot(time_series, value_b_series, label='value_b_series')
```

The lines each have a label.

--- /task ---

--- task ---

To finish off this function, a legend is added, and for the purposes of this example the `datetime.now()` value is auto-formatted so that it fits nicely on the `x` axis.

```python
    plt.legend()

    fig.autofmt_xdate()
```

--- /task ---

--- task ---

Now you can create an `animation` object. This will call the `animate` function every 1000 milliseconds, which is every second. It needs to be passed the `fig` object as the first parameter, and then the name of the function to be called.

```python
ani = animation.FuncAnimation(fig,
                              animate,
                              interval=1000)
```

--- /task ---

--- task ---

Lastly, you can display your plot.

```python
plt.show()
```

--- /task ---

