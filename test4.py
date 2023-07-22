from itertools import islice
# from signal import pause
# import keyboard


list_test = [1, 2, 3, 5, 7, 9, 44, 55, 33, 12, 12, 11, 90]

# print(list(islice(list_test, 2, 5)))

# for i in islice(list_test, 2, 5):
# print(i)


my_dict = {'a': 1, 'b': 2, 'c': [5, 6, 7, 8, 9],
           'd': 4, 'e': 5, 'f': [1, 2, 3, 4, 5]}
# print(len(my_dict))
finish = len(my_dict)
start = 0
step = 3
result = []
while start < finish:
    result.append(islice(my_dict.items(), start))
    start += step
print(result)

# for i in islice(my_dict.items(), 0, len, 2):
#     print(i)
    # keyboard.wait("space")


# search_text = "123" 
# search_items = ("name","phones", "email") 
# for item in search_items: 
#     if str(self.__dict__[item]).find(search_text) != -1: 
#         return True 
#     return False



# class Birthday(Field):
#    ...
    
# @property 
# def value(self): 
#     return self.__value @value.setter 

# def value(self, value:str) -> IncorrectDateFormat: 
#     today = datetime.now() 
#     birthday = datetime.strptime(value, r'%d-%m-%Y') 
#     if type(today) == type(birthday): 
#         self.__value = birthday 
#     else: 
#         raise IncorrectDateFormat


# today = date.today() 
# next_birthday = date( today.year, bday.month, bday.day) 
# if next_birthday < today: 
#     next_birthday = date(today.year + 1, bday.month, bday.day) 
#     return f"{(next_birthday - today).days} days left till birthday"