#!/usr/bin/python3
"""This is the user class"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref

from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    '''
    This is the class for user
    Attributes:
        email: the email address
        password: the password for your login
        first_name: user first name
        last_name: user last name
    '''
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship(
        "Place",
        cascade="all,delete",
        backref=backref("user", cascade="all,delete"),
        passive_deletes=True,
        single_parent=True)
    reviews = relationship(
        "Review",
        cascade="all,delete",
        backref=backref("user", cascade="all,delete"),
        passive_deletes=True,
        single_parent=True)
