from itertools import cycle
import time
import random

from sub.my_modul import my_func, VARIABLE


def mean():
    return 1


a = [22, 333, 555, 1, 77, 123, 456]


def my_map(func, data):
    result = []
    print('TAP 1')
    for itm in data:
        print('TAP 2')
        yield func(itm)
        print('TAP 3')
        yield itm
    print('TAP 4')


result = my_map(lambda x: x ** 3, a)

print(type(result))

while True:
    try:
        print(next(result))
    except StopIteration:
        break



# for itm in result:
#     print(itm)

# result = []
# for itm in range(1, 100):
#     if not itm & 1:
#         result.append(itm)


# print(result)
#
# result2 = [itm for itm in range(1, 100) if not itm & 1]
#
# print(result2)
# print(type(result) == type(result2))

# random_dict = {random.randint(1, 1000): random.random() for _ in range(1, 100)}
# random_dict2 = {random.randint(1, 1000): random.random() for _ in range(1, 100)}
# random_dict3 = {random.randint(1, 1000): random.random() for _ in range(1, 100)}
# random_dict4 = {random.randint(1, 1000): random.random() for _ in range(1, 100)}
#
# for itm in (random_dict, random_dict2, random_dict3, random_dict4):
#     print(len(itm))

print('HELLO MY FILE')
