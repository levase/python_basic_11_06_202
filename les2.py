"""
int - не из
float - не из
str - не из
bool - не из
list - изм
tuple - не изм
dict - изм
set - изм
frozenset - не изм
"""

my_str = 'HELLO my Dear Friends'
my_list = [1, 2, 3, 'hello']

my_dict = {'key1': 123, 1: 'fhhfhfh', 'key2': 'jfffgj'}

user = {
    'login': 'user1',
    'password': 'password string',
    'age': 22,
}

for value in my_list[:]:
    my_list.append(2222)
    print(my_list)
