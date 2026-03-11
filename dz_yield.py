from functools import reduce

numbers = [5, 12, 7, 20, 3, 18, 2, 15, 9, 30, 11, 6]

def greater_than_ten(numbers_list):
    for num in numbers_list:
        if num > 10:
            yield num


def square_numbers(numbers_list):
    for num in numbers_list:
        yield num ** 2

print(list(greater_than_ten(numbers)))
print(list(square_numbers(numbers)))

print(list(filter(lambda x: (x+1) % 2, square_numbers(numbers))))
print(list(map(lambda x: f"value = {x}", numbers)))

print(reduce(lambda a, b: a + b, numbers))
print(reduce(lambda a, b: a if a > b else b, numbers))

def multiples_of_three(n):
    for num in range(1, n+1):
        if num % 3 == 0:
            yield num

print(list(multiples_of_three(123)))

def word_generator(text):
    for word in text.split():
        yield word

text = "Da Da Net Net bolshoe_slovo i_eshe_odno"
print(list(word_generator(text)))
list_4 = filter(lambda x: len(x) > 4, word_generator(text))
print(list(map(lambda x: x.capitalize(), list_4)))


def fibonacci(n):
    last_res = 0
    last_res2 = 1
    yield last_res
    yield last_res2
    for cnt in range(n-2):
        res = last_res + last_res2
        yield res
        if cnt % 2 == 0:
            last_res = res
        else:
            last_res2 = res


# 0 1 2 выдают [0, 1] т.к у меня это база множества, которая всегда выдаётся
try:
    print(list(fibonacci(123)))
except Exception as e:
    print(e)