import unittest

from Database import Database
from Phonebook import Phonebook
from Contact import Contact

test_person_first_name = "Daniel"
test_person_last_name = "Hjartstrom"
test_person_phone_number = "0709522876"
test_person_address = "Tornby Park 15B"


def given_a_phonebook():
    return Phonebook()


def a_contact():
    return Contact(
        test_person_first_name,
        test_person_last_name,
        test_person_phone_number,
        test_person_address
    )


class TestStringMethods(unittest.TestCase):

    def test_phonebook_is_not_null(self):
        phonebook = given_a_phonebook()
        assert phonebook is not None

    def test_add_single_person(self):
        phonebook = given_a_phonebook()
        phonebook.add_new_contact(a_contact())
        assert phonebook.count() == 1

    def test_add_two_people(self):
        phonebook = given_a_phonebook()
        phonebook.add_new_contact(a_contact())
        phonebook.add_new_contact(a_contact())
        assert phonebook.count() == 2

    def test_create_contact_object(self):
        contact = a_contact()
        assert contact is not None

    def test_contact_first_name_not_empty(self):
        contact = a_contact()
        assert contact.firstname != ""

    def test_contact_last_name_not_empty(self):
        contact = a_contact()
        assert contact.lastname != ""

    def test_contact_phone_number_not_empty(self):
        contact = a_contact()
        assert contact.phone_number != ""

    def test_contact_address_not_empty(self):
        contact = a_contact()
        assert contact.address != ""

    def test_database_instance_not_none(self):
        database = Database()
        assert database.DBSession is not None

    def test_add_contact_to_database(self):
        database = Database()
        database.add_new_contact(a_contact())
        database.get_all_contacts()
        assert len(database.contacts) == 1

    def test_remove_single_contact_by_id(self):
        database = Database()
        contact = a_contact()
        database.add_new_contact(contact)
        database.get_all_contacts()
        single_contact = database.contacts[0]
        database.remove_contact_by_id(single_contact)
        database.get_all_contacts()
        assert len(database.contacts) == 0


if __name__ == '__main__':
    unittest.main()
