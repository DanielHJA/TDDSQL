from sqlalchemy import Column, Integer, String
from Base import Base


class Contact(Base):
    __tablename__ = 'Contacts'

    id = Column(Integer(), primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    phone_number = Column(String(50))
    address = Column(String(100), nullable=True)

    def __init__(self, firstname, lastname, phone_number, address):
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number
        self.address = address
