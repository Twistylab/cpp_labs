import time
import csv
import pandas as pd

def calculate(x=10):
    return x**2 - x**2 + x*4 - x*5 + x + x

if __name__ == "__main__":
    data = {"time": [], "n": []}
    for n in range(int(1e3), int(1e6), int(1e3)):
        start_time = time.time()
        duration = 0
        for i in range(n):
            res = calculate()
        end_time = time.time()
        duration = end_time - start_time
        data["time"].append(duration)
        data["n"].append(n)
    with open('result_py.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data.keys())

        for row in zip(*data.values()):
            writer.writerow(row)
