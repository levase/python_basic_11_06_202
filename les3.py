def my_sum(data):
    result = 0
    for itm in data:
        result += itm
    return result


def test(x):
    return x ** 3


def my_map(func, data: list) -> list:
    """это моя реализаци MAP
    :param func: функция которая применится к объектам итератора
    :param data: итерируемый объект
    :return: список резултатов
    """
    result = []
    for itm in data:
        result.append(func(itm))
    return result


a = [2, 3, 4, 5]


def test2(data):
    print(id(data))
    data.append('fjgfjgfj')
    print(data)


def test3(x, y, z, w):
    print(x, y, z, w)
    # return sum([x, y, z, w])


def test_4(*args, **kwargs):
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)


x = 2
y = 3
z = 4
w = 5

# tmp_list = [2, 3, 4, 5]
# tmp_str = '2345'
# res = test3(*tmp_str)

# res = test_4(1, 2, 3, 4, 5, 6, 7, 8, 9, data1=33, data2='fhfhhf', hello=444)

# print(id(a))
# print(a)
# test2(a[:])
# print(a)

# res = sum(a)
# print(res)
# print('#' * 30)
# new_res = my_sum(a)
# print(new_res)
# print('#' * 30)
res: list = list(map(lambda x: x ** 3, a))
print(res)
# print('#' * 30)
new_res = my_map(test, a)
# print(new_res)


template = {
    'data1': ('ask', lambda x: int(x) ** 2)
}

for key, value in template.items():
    test = input(value[0])
    print(value[1](test))
