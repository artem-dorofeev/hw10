my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# # Створення ітератора
# iterator = iter(my_dict.items())

# # Використання next() для отримання наступного значення
# print(next(iterator))  # Виведе 1
# print(next(iterator))  # Виведе 2
# print(next(iterator))  # Виведе 3

# # Перебір значень за допомогою циклу for
# for value in my_dict.values():
#     print(value)  # Виведе 1, 2, 3

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


# Використання власного ітератора по словнику
my_dict = {'apple': 1, 'banana': 2, 'orange': 3, 'kiwi': 4}
iterator = DictionaryIterator(my_dict, 5)

for key in iterator:
    print(key)  # Виведе ключі, довжина яких не перевищує 5

"""
У цьому прикладі клас DictionaryIterator приймає словник та максимальну довжину ключа як аргументи конструктора. 
Метод __iter__() повертає сам ітератор, а метод __next__() перебирає ключі словника відповідно до заданого обмеження довжини. 
Коли всі відповідні ключі перебрано, піднімається виняток StopIteration.

Це простий приклад створення власного ітератора по словнику з визначеними правилами перебору. 
Ви можете модифікувати логіку ітератора відповідно до ваших потреб.

"""
