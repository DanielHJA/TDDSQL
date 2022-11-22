class Phonebook:

    def __init__(self):
        self.contacts = []

    def add_new_contact(self, contact):
        self.contacts.append(contact)

    def count(self):
        return len(self.contacts)
