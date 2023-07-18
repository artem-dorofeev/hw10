from collections import UserDict
from collections.abc import Iterator
from datetime import datetime


class Field:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return str(self)


class Name(Field):
    ...


class Phone(Field):
    ...


class Birth(Field):
    def __init__(self, *value) -> None:
        # self.name = value[0]
        # print(f'Birth print 1 {self.name}')
        self.time = value[0]
        print(f"birth print2 {datetime.strptime(self.time, '%d.%m.%Y')}")
        super().__init__(value)

    def ___str___(self):
        return datetime.strptime(self.time, '%d.%m.%Y')


class Record:
    def __init__(self, name: Name, phone: Phone = None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone: Phone):
        if phone.value not in [p.value for p in self.phones]:
            self.phones.append(phone)
            return f"Телефон {phone} додано до контакту {self.name}"
        return f"{phone} вже є у контакта {self.name}"

    def change_phone(self, old_phone, new_phone):
        for idx, p in enumerate(self.phones):
            if old_phone.value == p.value:
                self.phones[idx] = new_phone
                return f"старий номер {old_phone} змінено на {new_phone}"
        return f"{old_phone} відсутній в списку контакта {self.name}"

    def __str__(self) -> str:
        return f"{self.name}: {', '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[str(record.name)] = record
        # print(self.data)
        return f"Контакт {record} додано успішно"

    def __iter__(self) -> Iterator:
        # self.curent_index = 0
        return self

    def __next__(self):
        for key, value in self.data.items():
            return f"it`s OK {key} : {value}"
        raise StopIteration

    def __getitem__(self, key):
        return super().__getitem__(key)

    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.data.values())
