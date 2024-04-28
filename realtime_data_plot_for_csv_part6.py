import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
from pathlib import Path

csv_file_path_name = Path(Path.cwd(), 'datasets', 'fake_csv_data', 'data.csv')

plt.style.use('fivethirtyeight')



def updateRealTimeDataInList(frame_number):

    data = pd.read_csv(csv_file_path_name)
    x_data = data['x_data']
    price_in_us = data['price_in_us']
    price_in_jp = data['price_in_jp']

    plt.cla()
    plt.plot(x_data, price_in_us, label='US price')
    plt.plot(x_data, price_in_jp, label='Japan price')

    plt.legend(loc='upper left')
    plt.tight_layout()


capture_updated_data_on_Plot = FuncAnimation(plt.gcf(), updateRealTimeDataInList, interval=1000)

plt.show()