class contact:
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

    def get_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_birthday(self):
        return self.birthday

    def set_birthday(self, birthday):
        self.birthday = birthday


class address_book:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def edit_contact(self, contact, new_contact):
        index = self.contacts.index(contact)
        self.contacts[index] = new_contact