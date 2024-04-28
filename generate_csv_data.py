import csv
import random
import time
from pathlib import Path
import sys

csv_file_path_name = Path(Path.cwd(), 'datasets', 'fake_csv_data', 'data.csv')

try: 
    csv_file_path_name.mkdir(parents=True, exist_ok=True)
except Exception as err:
    print(err)
    sys.exit()

header_column_names = ['x_data', 'price_in_us', 'price_in_jp']
x_data = 0
price_in_us = 1000
price_in_jp = 1000


with open(csv_file_path_name, 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=header_column_names)
    csv_writer.writeheader()

while True:

    with open(csv_file_path_name, 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=header_column_names)

        info = {
            "x_data"  : x_data,
            "price_in_us" : price_in_us,
            "price_in_jp" : price_in_jp
        }

        csv_writer.writerow(info)
        print(x_data, price_in_us, price_in_jp)

        x_data += 1
        price_in_us = price_in_us + random.randint(-9, 9)
        price_in_jp = price_in_jp + random.randint(-5, 5)

    time.sleep(2)
