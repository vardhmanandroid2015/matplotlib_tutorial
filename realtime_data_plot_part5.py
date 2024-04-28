import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import random

plt.style.use('fivethirtyeight')

index = count()
print(index)

x_data, y_data = list(), list()

def updateRealTimeDataInList(frame_number):

    x_data.append(next(index))
    y_data.append(random.randint(1, 8))

    plt.cla()
    plt.plot(x_data, y_data)

capture_updated_data_on_Plot = FuncAnimation(plt.gcf(), updateRealTimeDataInList, interval=1000)

plt.show()