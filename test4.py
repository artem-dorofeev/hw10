from itertools import islice
from signal import pause
import keyboard


list_test = [1, 2, 3, 5, 7, 9, 44, 55, 33, 12, 12, 11, 90]

# print(list(islice(list_test, 2, 5)))

# for i in islice(list_test, 2, 5):
# print(i)


my_dict = {'a': 1, 'b': 2, 'c': [5, 6, 7, 8, 9],
           'd': 4, 'e': 5, 'f': [1, 2, 3, 4, 5]}
print(len(my_dict))
len = len(my_dict)

for i in islice(my_dict, len):
    print(i)
    keyboard.wait("space")
