import numpy as np

class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.counter = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > self.n:
            raise StopIteration

        res = self.counter
        self.counter += 2
        return res


for x in EvenIterator(10):
    print(x)

print("====================================")

class ReverseList:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        res = self.lst[self.index]
        self.index -= 1
        return res


for x in ReverseList([10, 20, 30, 40, 50]):
    print(x)

print("====================================")
arr = np.array([3, 7, 1, 9, 4])
print(arr.max())
print(np.mean(arr))

print("====================================")
arr = np.array([2, 8, 4, 10, 3])
print(arr[arr > 5])

print("====================================")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a+b)

print("===================================")
arr = np.array([1, 2, 3, 4])
print(arr * 2)