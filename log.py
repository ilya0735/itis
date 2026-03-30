from datetime import datetime
import re
import time


def time_dimension(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return f"Функция {func.__name__} выполнена за {end - start} секунд"
    return wrapper


dict_of_logs = {}
@time_dimension
def log_formating():
    try:
        with open("log.log", "r") as log:
            log_file = log.readlines()
    except FileNotFoundError:
        print("Файл не найден")

    list_of_logs = []
    for line in log_file:
        if line == "\n":
            break
        parts = re.split(r'(?<=\])\s+|:\s+', line)
        list_of_logs.append(parts)

    for log in list_of_logs:
        log[2] = re.sub('\n', '', log[2])
        log[0] = datetime.strptime(log[0].replace("[", "").replace("]", ""), "%Y-%m-%d %H:%M:%S")
        if log[1] in dict_of_logs:
            dict_of_logs[log[1]].append([log[0], log[2]])
        else:
            dict_of_logs[log[1]] = [[log[0], log[2]]]


def session_time(name):
    try:
        login_date = None
        logout_date = None
        for log in reversed(dict_of_logs[name]):
            if log[1] == "login":
                login_date = log[0]
                break
            elif log[1] == "logout":
                logout_date = log[0]
        return logout_date-login_date
    except TypeError:
        return f"{name} не закончил сессию"



log_formating()
for user in dict_of_logs.keys():
    print("===================================================================================")
    print(f"Пользователь {user} провел в системе: {session_time(user)}")
    if len(dict_of_logs[user]) > 1:
        if str(len(dict_of_logs[user])-2)[-1] == "1":
            print(f"Пользователь {user} сделал {len(dict_of_logs[user])-2} действие")
        elif str(len(dict_of_logs[user])-2)[-1] in "234":
            print(f"Пользователь {user} сделал {len(dict_of_logs[user])-2} действия")
        else:
            print(f"Пользователь {user} сделал {len(dict_of_logs[user]) - 2} действий")
    else:
        print(f"Пользователь {user} сделал 0 действий")

