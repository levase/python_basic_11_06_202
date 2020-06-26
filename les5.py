import os
from os import path
import json

import requests

# url = 'https://5ka.ru/api/v2/special_offers/'
# ya_url = 'https://ya.ru/'
#
# response = requests.get(url)
#
# print(response.json())
# data = response.json()

# for itm in data['results']:
#     with open(f"{itm['id']}.json", 'w', encoding='UTF-8') as file:
#         json.dump(itm, file, ensure_ascii=False)

this_dir = path.dirname(__file__)
dir_files = [path.join(this_dir, itm) for itm in os.listdir(this_dir) if itm.split('.')[-1] == 'json']

res = []
for itm in dir_files:
    with open(itm, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        res.append(data)

print([type(itm) for itm in res])
print(res)

# data = [
#     {'name': 'Вася', 'surname': 'Иванов', 'age': 22, 'salary': 12000, 'driver': True, 'a': (1, 2, 3, 4)},
#     {'name': 'Вася2', 'surname': 'Иванов2', 'age': 22, 'salary': 12000, 'driver': False},
#     {'name': 'Вася3', 'surname': 'Иванов3', 'age': None, 'salary': 12000, 'driver': True},
#     {'name': 'Вася4', 'surname': 'Иванов4', 'age': 22, 'salary': 11113.5, 'driver': True}
# ]

# j_data = json.dumps(data, ensure_ascii=False)
# print(type(j_data))
# print(j_data)

# with open('new_file2.json', 'r', encoding='UTF-8') as file:
#     # json.dump(data, file, ensure_ascii=False)
#     data = json.load(file)
#
# print(type(data[0]))
# print(data)
# file = open('les5.txt', 'a', encoding='UTF-8')
#
# try:
#     file.write('Hello new string')
# except FileExistsError:
#     pass
# finally:
#     file.close()


# with open('les5.txt', 'w', encoding='UTF-8') as file:
#     for n in range(1, 100):
#         file.write(f'{n} --- string\n')

# with open('les5.txt', 'r') as file, open('les5_1.txt', 'w') as file_1:
#     file_1.write(file.read())
# for line in file:
#     print(line, end='')
# print(file.readlines())
# print(file.read(8))
# print(file.read(8))
# print(file.tell())
# file_name = 'new_name.txt'
# current_path = path.dirname( __file__)
#
# # for itm in os.listdir(current_path):
# #     temp_path = path.join(current_path, itm)
# #     print(itm, path.isdir(temp_path))
#
# os.rename(path.join(current_path, file_name), 'new_name')
#
#
#
# print()
