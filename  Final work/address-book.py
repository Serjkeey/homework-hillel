class Contact:
    def __init__(self, name, surname, phone_number, address='', birthday=''):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.address = address
        self.birthday = birthday

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.surname = surname

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_birthday(self):
        return self.birthday

    def set_birthday(self, birthday):
        self.birthday = birthday


import pickle
import os


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def edit_contact(self, contact, new_contact):
        index = self.contacts.index(contact)
        self.contacts[index] = new_contact

    def search_by_name(self, name):
        results = []
        for contact in self.contacts:
            if contact.get_name().lower() == name.lower():
                results.append(contact)
        return results

    def search_by_phone_number(self, phone_number):
        results = []
        for contact in self.contacts:
            if contact.get_phone_number() == phone_number:
                results.append(contact)
        return results

    def sort_by_name(self):
        self.contacts.sort(key=lambda contact: contact.get_name())

    def sort_by_surname(self):
        self.contacts.sort(key=lambda contact: contact.get_surname())

    def load_contacts_from_file(self, file_name):
        if os.path.exists(file_name):
            with open(file_name, 'rb') as file:
                self.contacts = pickle.load(file)
                print(f"Завантажено {len(self.contacts)} записів з файлу.")
        else:
            print("Файл зі збереженими даними не знайдено.")

    def save_contacts_to_file(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(self.contacts, file)
            print(f"Записи збережено у файл {file_name}.")


address_book = AddressBook()
file_name = "contacts.dat"
address_book.load_contacts_from_file(file_name)

while True:
    print("\nМеню:")
    print("1. Добавити запис")
    print("2. Видалити запис")
    print("3. Редагувати запис")
    print("4. Пошук за ім'ям")
    print("5. Пошук за номером телефону")
    print("6. Сортувати за ім'ям")
    print("7. Сортувати за прізвищем")
    print("8. Вийти")

    choice = input("Зробіть ваш вибір: ")

    if choice == '1':
        name = input("Введіть ім'я: ")
        surname = input("Введіть прізвище: ")
        phone_number = input("Введіть номер телефону: ")
        address = input("Введіть адресу (необов'язково): ")
        birthday = input("Введіть дату народження (необов'язково): ")
        contact = Contact(name, surname, phone_number, address, birthday)
        address_book.add_contact(contact)
        print("Запис додано.")

    elif choice == '2':
        name = input("Введіть ім'я запису, який бажаєте видалити: ")
        matching_contacts = address_book.search_by_name(name)
        if len(matching_contacts) > 0:
            for index, contact in enumerate(matching_contacts):
                print(f"{index + 1}. {contact.get_name()} {contact.get_surname()}")
            selection = input("Виберіть номер запису для видалення: ")
            if selection.isdigit() and int(selection) <= len(matching_contacts):
                contact_to_remove = matching_contacts[int(selection) - 1]
                address_book.remove_contact(contact_to_remove)
                print("Запис видалено.")
            else:
                print("Некоректний вибір.")
        else:
            print("Записів не знайдено.")

    elif choice == '3':
        name = input("Введіть ім'я запису, який бажаєте редагувати: ")
        matching_contacts = address_book.search_by_name(name)
        if len(matching_contacts) > 0:
            for index, contact in enumerate(matching_contacts):
                print(f"{index + 1}. {contact.get_name()} {contact.get_surname()}")
            selection = input("Виберіть номер запису для редагування: ")
            if selection.isdigit() and int(selection) <= len(matching_contacts):
                contact_to_edit = matching_contacts[int(selection) - 1]
                new_name = input("Введіть нове ім'я: ")
                new_surname = input("Введіть нове прізвище: ")
                new_phone_number = input("Введіть новий номер телефону: ")
                new_address = input("Введіть нову адресу (необов'язково): ")
                new_birthday = input("Введіть нову дату народження (необов'язково): ")
                new_contact = Contact(new_name, new_surname, new_phone_number, new_address, new_birthday)
                address_book.edit_contact(contact_to_edit, new_contact)
                print("Запис відредаговано.")
            else:
                print("Некоректний вибір.")
        else:
            print("Записів не знайдено.")

    elif choice == '4':
        name = input("Введіть ім'я для пошуку: ")
        matching_contacts = address_book.search_by_name(name)
        if len(matching_contacts) > 0:
            for contact in matching_contacts:
                print(f"{contact.get_name()} {contact.get_surname()}: {contact.get_phone_number()}")
        else:
            print("Записів не знайдено.")

    elif choice == '5':
        phone_number = input("Введіть номер телефону для пошуку: ")
        matching_contacts = address_book.search_by_phone_number(phone_number)
        if len(matching_contacts) > 0:
            for contact in matching_contacts:
                print(f"{contact.get_name()} {contact.get_surname()}: {contact.get_phone_number()}")
        else:
            print("Записів не знайдено.")

    elif choice == '6':
        address_book.sort_by_name()
        print("Записи відсортовано за ім'ям.")

    elif choice == '7':
        address_book.sort_by_surname()
        print("Записи відсортовано за прізвищем.")

    elif choice == '8':
        address_book.save_contacts_to_file(file_name)
        print("Записи збережено у файл.")
        break

    else:
        print("Некоректний вибір. Спробуйте ще раз.")


