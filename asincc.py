import asyncio
from threading import Thread
import time
import random
import multiprocessing

# def order(order_id):
#     time.sleep(random.randint(1,2))
#     for i in range(random.randint(1,250_000)):
#         i**2 + i%2
#     print(f"Заказ {order_id} обработан")
#
# start = time.time()
# thread1 = Thread(target=order, args=(1,))
# thread2 = Thread(target=order, args=(2,))
# thread3 = Thread(target=order, args=(3,))
# thread4 = Thread(target=order, args=(4,))
# thread5 = Thread(target=order, args=(5,))
# threads = [thread1, thread2, thread3, thread4, thread5]
# for thread in threads:
#     thread.start()
# for thread in threads:
#     thread.join()
# end = time.time()
# print(end - start)
#
# start = time.time()
# for i in range(5):
#     order(i+1)
# end = time.time()
# print(end - start)



# def func(n):
#     res = 0
#     for _ in range(10**7):
#         res += (n/2*1337)**n
#     return res
#
# if __name__ == '__main__':
#     start = time.time()
#     with multiprocessing.Pool() as p:
#         result = p.map(func, range(5))
#         print(result)
#     end = time.time()
#     print(end - start)

#
#
# async def async_order(user_id):
#     await asyncio.sleep(random.randint(1, 2))
#     numbers = []
#     for _ in range(500_000):
#         numbers.append(random.randint(1, 10))
#     sum(numbers)
#     print(f'Запрос пользователя {user_id} выполнен ')
#
# async def main():
#     lst = []
#     for i in range(10):
#         lst.append(async_order(i))
#     await asyncio.gather(*lst)
#
# if __name__ == '__main__':
#     asyncio.run(main())




def universal(task_id):
    time.sleep(1)
    n = 0
    for i in range(10**6):
        n += (i ** 2)//(123+i)
    time.sleep(1)
    return n





if __name__ == '__main__':
    start = time.time()
    for i in range(5):
        print(universal(i))
    end = time.time()
    print(f"sync: {end - start}")


    threads = []
    for i in range(5):
        threads.append(Thread(target=universal, args=(i,)))
    start = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end = time.time()
    print(f"async: {end - start}")


    start = time.time()
    with multiprocessing.Pool() as p:
        result = p.map(universal, range(5))
        print(result)
    end = time.time()
    print(f"multiprocessing: {end - start}")






