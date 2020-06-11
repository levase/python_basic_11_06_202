# PEP8

"""
int - Это целое число
float - Это Дробное число
str - это строка
bool - boolean всего 2 значения Истины = True Ложь = False
"""

catalog_id_1 = 14  # Это комментарий
catalog_id_2 = 15
my_float = 12.134
my_str1 = 'Это строка 1'
my_str2 = "Это тоже строка 2"
my_str3 = """"то строка из
множества
строк"""

my_str4 = 'Нужно выделить "ТЕРМИН"'
my_str5 = "Нужно выделить \"ТЕРМИН\""

# age = 33
#
# if age >= 18:
#     print('Доступ разрешен')
# elif age >= 16:
#     print('Ограниченный доступ')
# else:
#     print('Доступ запрещен')
#
# while True:
#     age = input('Введите возраст\n')
#     if not age.isdigit():
#         print('возраст должен быть числом')
#         continue
#     age = int(age)
#     break
#
# if age >= 18:
#     print('Доступ разрешен во все разделы включая XXX')
# elif age >= 16:
#     print('Доступ разрешен во все разделы')
# elif age >= 8:
#     print('Доступ разрешен в раздел мультики')
# else:
#     print('Доступ запрещен')

# while True:
#     user = input()
#     if user == 'a':
#         continue
#     print(user)


name = 'USER'
surname = 'LAMER'
age = 16

'Пример User, тебе 16 лет твоя фамилия LAMER'

result = 'Пример {n:^20}, тебе {a} лет твоя фамилия {s}'.format(a=age, n=name, s=surname)
f_result = f'Пример {name:^20}, тебе {age} лет твоя фамилия {surname}, {2020 - age} года рождения'
print(f_result)
