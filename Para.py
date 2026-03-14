from functools import reduce

import numpy as np
temperatures = np.random.randint(-20, 40, 1000)


def flow(temperature_list):
    for temperature in temperature_list:
        if -16 < temperature < 36:
            yield temperature

def normalize(x, lst):
    return (x - np.mean(lst)) / np.std(lst)

def next_normalize(x):
    return np.sin(x) + x**2

def group(group_list):
    for temperature in group_list:
        yield temperature

anomaly_groups = []
group_30 = []
count_of_group = 0
for temp in flow(temperatures):
    normalized_temp = next_normalize(normalize(temp, list(flow(temperatures))))
    group_30.append(normalized_temp)
    if len(group_30) == 30:
        count_of_group += 1
        group1 = group(group_30)
        temperature_list = list(group1)

        mean_temp = np.mean(temperature_list)
        median_temp = np.median(temperature_list)
        std_temp = np.std(temperature_list)
        min_temp = np.min(temperature_list)
        max_temp = np.max(temperature_list)
        if abs(mean_temp) > 1 or std_temp > 1:
            anomaly_groups.append(temperature_list)
        group_30.clear()

print(f"Всего окон: {count_of_group}")
print(f"Аномальных окон: {len(anomaly_groups)}")
print(f"Максимальное среднее значение: {reduce(lambda a, b: a if a > b else b, [np.mean(x) for x in anomaly_groups])}")
print(f"Сумма средних значений: {reduce(lambda x, y: x + y, [np.mean(x) for x in anomaly_groups])}")











