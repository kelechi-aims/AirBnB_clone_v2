#!/usr/bin/python3
""" New engine DBStorage """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review

instances = {"State": State, "City": City, "Amenity": Amenity,
             "User": User, "Review": Review, "Place": Place}


class DBStorage:
    """ Private class attributes for able creation """
    __engine = None
    __session = None

    def __init__(self):
        """ Create the engine (self.__engine) """
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db)
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

 def all(self, cls=None):
        '''
        Prints all objects in the database
        '''
        instlist = [State, City, User]
        new_dict = {}
        if cls:
            for obj in self.__session.query(instances[cls]).all():
                key = str(obj.__class__.__name__) + "." + str(obj.id)
                value = obj
                new_dict[key] = value
            return new_dict
        else:
            for inst in instlist:
                for obj in self.__session.query(inst).all():
                    key = str(inst.__name__) + "." + str(obj.id)
                    value = obj
                    new_dict[key] = value
            return new_dict

def reload(self):
        '''
        Create the current database session
        '''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def new(self, obj):
        """ Add the object to the current database session """
        if obj:
            self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        '''
        Delete from the current database session obj if not None
        '''
        if obj:
            self.__session.delete(obj)

    def close(self):
        """ calls on remove """
        self.__session.remove()
