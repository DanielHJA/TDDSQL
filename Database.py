from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Contact import Contact


class Database:

    def __init__(self):
        self.contacts = []
        self.__setup_connection()
        # Clear table before each run
        self.clear_table()

    def __setup_connection(self):
        user = 'root'
        password = 'root'
        host = 'localhost'
        port = 8889
        database = 'Phonebook'

        engine = create_engine(
            url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
                user, password, host, port, database), echo=True)

        self.DBSession = sessionmaker(bind=engine)

    def clear_table(self):
        session = self.DBSession()
        try:
            session.query(Contact).delete()
            session.commit()
        except:
            session.rollback()
        session.close()

    def add_new_contact(self, contact):
        session = self.DBSession()
        try:
            session.add(contact)
            session.commit()
        except:
            session.rollback()
        session.close()

    def get_all_contacts(self):
        session = self.DBSession()
        results = session.query(Contact).all()
        self.contacts = results
        session.close()

    def remove_contact_by_id(self, contact):
        session = self.DBSession()
        try:
            session.query(Contact).filter(Contact.id == contact.id).delete()
            session.commit()
        except:
            session.rollback()
        session.close()
