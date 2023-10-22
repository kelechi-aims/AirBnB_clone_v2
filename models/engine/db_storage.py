#!/usr/bin/python3
"""
Module db_storage
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.review import Review

db = getenv("HBNB_MYSQL_DB")
host = getenv("HBNB_MYSQL_HOST")
passwd = getenv("HBNB_MYSQL_PWD")
user = getenv("HBNB_MYSQL_USER")
env = getenv("HBNB_ENV")


class DBStorage():
    """
    DBStorage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Creates the engine
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Prints all objects in the database
        """
        obj_dict = {}
        if cls:
            objects = self.__session.query(cls).all()
        else:
            objects = []
            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                objects += self.__session.query(cls).all()
        for obj in objects:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database (feature of SQLAlchemy)"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Scoped = scoped_session(Session)
        self.__session = Scoped

    def close(self):
        """
        Call remove() method on the private session attribute (self.__session).
        """
        self.__session.close()
