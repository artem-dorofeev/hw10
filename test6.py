from collections import UserDict
from itertools import islice

class AdrBook(UserDict):
    def add_record(self, **value):
        self.data[str(value.keys())] = value.values()
        # print(self.data)
        # print(len(self.data))
        # print(str(self))
        # print()
        return f"Контакт {self.keys()} додано успішно"
    
    def iterator(self, n=3):
        result = ''
        # count = 0
        # for cont in self.items():
        #     result += str(cont[0]) + " : " + str(cont[1]) + "\n"
        #     # print(cont)
        #     # result += "{cont[key]} : " + "{cont[value]}" + "\n" 
        #     count +=1
        #     if count >= n:
        #         yield result
        #         count = 0
        #         result = ""
        # if result:
        #     yield result
        
        long = len(self.data)
        # result = islice(self.items(), 0, 5, 2)
        for cont in islice(self.items(), 0, 5, 2):
            # result += str(cont[0]) + " : " + str(cont[1]) + "\n"
            result += cont + "\n"
            yield result
        



my_dict = {'Artem': '0506667755', 'Ira': '0509998877', 'Diana': '0674445566',
           'Mila': '0678887766', 'Test': '030554433', 'Ira22': '0509998877'}

my_dict2 = {'Artem2': '0506667755'}
new_dict = AdrBook(my_dict)
# print(new_dict)

# new_dict.add_record(**my_dict2)
# print(new_dict)

for i in new_dict.iterator():
    print(i)

# test = islice(my_dict.items(), 0, len(my_dict), 2)

# print(next(test))
# print(next(test))
# print(next(test))