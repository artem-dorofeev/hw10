from collections import UserDict
from collections.abc import Iterator
from datetime import datetime


class AdrBook(UserDict):
    def add_record(self, record):
        self.data[str(record)] = record
        return f"Контакт {record} додано успішно"

    def __iter__(self) -> Iterator:
        return self

    def __next__(self):
        pass


class DictionaryIterator:
    def __init__(self, dictionary, max_key_length):
        self.dictionary = dictionary
        self.max_key_length = max_key_length
        self.keys = list(dictionary.keys())
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_index < len(self.keys):
            key = self.keys[self.current_index]
            value = self.dictionary[key]
            self.current_index += 1
            if len(key) <= self.max_key_length:
                return f'{key} - {value}'
        raise StopIteration


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
iterator = DictionaryIterator(my_dict, 5)

for key in iterator:
    print(key)

# print(iterator)
# new_dict = AdrBook(my_dict)
# new_dict2 = AdrBook()
# print(type(new_dict))
# print(type(new_dict2))
# print(new_dict['a'])
# new_dict['g'] = 10
# print(new_dict)
# new_dict2['r'] = 2
# print(new_dict2)
