#!/usr/bin/python3
"""Module for setting up a MySQL engine"""

import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """Handles MySQL database engine creation and session management"""

    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the engine and drops tables if in test environment"""
        self.__engine = create_engine(
            f"mysql+mysqldb://{os.getenv('HBNB_MYSQL_USER')}:" +
            f"{os.getenv('HBNB_MYSQL_PWD')}@" +
            f"{os.getenv('HBNB_MYSQL_HOST')}/" +
            f"{os.getenv('HBNB_MYSQL_DB')}",
            pool_pre_ping=True
        )
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of all objects in the session"""
        obj_dict = {}
        if cls:
            cls = self.classes.get(cls)
            if cls:
                objects = self.__session.query(cls).all()
            else:
                return obj_dict
        else:
            objects = self.__session.query(
                State, City, User, Amenity, Place, Review).all()
        for obj in objects:
            key = f"{obj.__class__.__name__}.{obj.id}"
            obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Adds an object to the session"""
        self.__session.add(obj)
        self.__session.flush()

    def save(self):
        """Commits the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates tables and establishes the session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes the current session"""
        if self.__session:
            self.__session.remove()
