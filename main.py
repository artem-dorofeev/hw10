from sanitize import sanitize_phone_number
from classes_bot import AddressBook, Name, Phone, Record


contacts_dict = AddressBook()


def input_error(func):
    def wrapper(x):
        try:
            result = func(x)
        except IndexError:
            return f"Введіть ім'я та номер контакту"
        return result
    return wrapper


def index_error(func):
    def wrapper(x):
        try:
            result = func(x)
        except IndexError:
            return f'Немає імені контакту'
        return result
    return wrapper


def hello_func(text=None):
    return f'Привіт, чим можу допомогти?'


@input_error
def add_func(args: list):
    name = Name(args[0].capitalize())
    phone = Phone(sanitize_phone_number(args[1]))
    rec: Record = contacts_dict.get(str(name))
    if rec:
        return rec.add_phone(phone)
    rec = Record(name, phone)
    contacts_dict.add_record(rec)
    return f'До адресної книги додан контакт {name.value} - {phone.value}'


def show_all(text=None):
    return contacts_dict


@input_error
def change_command(args: list):
    name = Name(args[0].capitalize())
    old_phone = Phone(sanitize_phone_number(args[1]))
    new_phone = Phone(sanitize_phone_number(args[2]))
    rec: Record = contacts_dict.get(str(name))
    if rec:
        return rec.change_phone(old_phone, new_phone)
    return f"Немає {name} в списку кнтактів"


@index_error
def phone_print(data):
    contact = data[0].capitalize().strip()
    for key, val in contacts_dict.items():
        
        if contact == key:
            print(key)
            return f'Контакт: {val}'
    return f'Немає {contact} в списку контактів'


def exit_command(*args):
    return f'До побачення'

def unknown_command(*args):
    return f'Невідома команда'

COMMAND_DICT = {
    hello_func: ("hello", "hi", "привіт"),
    add_func: ("add", "+", "додати"),
    show_all: ("show all", "показати все"),
    change_command: ("change", "змінити"),
    phone_print: ("phone", "друк"),
    exit_command: ("до побачення", "до зустрічі", "exit", "by", "пока")
}

def parser_text(text:str):
    for cmd, kwds in COMMAND_DICT.items():
        for kwd in kwds:
            if text.lower().startswith(kwd):
                data = text[len(kwd):].strip().split()
                return cmd, data 
    return unknown_command, []

def main():

    while True:

        user_input = input('>>чекаю ввод>>')
        cmd, data = parser_text(user_input)
        result = cmd(data)
        if cmd == exit_command:
            print(result)
            break
        print(result)

if __name__ == "__main__":
    main()
