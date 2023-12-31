from classes_bot import AddressBook, Name, Phone, Record
from sanitize import sanitize_phone_number

address_book = AddressBook()


def input_error(func):
    def wrapper(*args):
        try:
            result = func(*args)
        except IndexError:
            return f"Введіть ім'я та номер контакту"
        return result
    return wrapper


@input_error
def add_command(*args):
    name = Name(args[0].capitalize())
    phone = Phone(sanitize_phone_number(args[1]))
    rec: Record = address_book.get(str(name))
    if rec:
        return rec.add_phone(phone)
    rec = Record(name, phone)
    return address_book.add_record(rec)


def index_error(func):
    def wrapper(*args):
        try:
            result = func(*args)
        except IndexError:
            return f"Немає імені або номеру контакта"
        return result
    return wrapper


@index_error
def phone_print(*data):
    contact = data[0].capitalize().strip()
    for key, val in address_book.items():
        
        if contact == key:
            print(key)
            return f"Контакт: {val}"
    return f"Немає {contact} в списку контактів"

@index_error
def change_command(*args):
    name = Name(args[0].capitalize())
    old_phone = Phone(sanitize_phone_number(args[1]))
    new_phone = Phone(sanitize_phone_number(args[2]))
    rec: Record = address_book.get(str(name))
    if rec:
        return rec.change_phone(old_phone, new_phone)
    return f"Немає {name} в списку кнтактів"

def hello_func(text=None):
    return f"Привіт, чим можу допомогти?"

def exit_command(*args):
    return "До побачення"


def unknown_command(*args):
    return f"Невідома команда"


def show_all_command(*args):
    return address_book


COMMANDS = {
    add_command: ("add", "+", "додати"),
    change_command: ("change", "зміни"),
    exit_command: ("до побачення", "до зустрічі", "exit", "by", "пока", "end"),
    show_all_command: ("show all", "показати все"),
    hello_func: ("hello", "hi", "привіт"),
    phone_print: ("phone", "друк", "print")
}


def parser(text:str):
    for cmd, kwds in COMMANDS.items():
        for kwd in kwds:
            if text.lower().startswith(kwd):
                data = text[len(kwd):].strip().split()
                return cmd, data 
    return unknown_command, []

def main():
    while True:
        user_input = input(">>чекаю ввод>>")
        cmd, data = parser(user_input)
        result = cmd(*data)
        print(result)
        if cmd == exit_command:
            break

if __name__ == "__main__":
    main()