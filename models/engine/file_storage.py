#!/usr/bin/python3
"""This module handles file storage for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Manages JSON file serialization and deserialization
    Attributes:
        __file_path: path to the JSON file
        __objects: stores objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of stored objects
        Args:
            cls: Optional class type to filter objects
        Returns:
            Dictionary of objects matching the class type
        """
        result = {}
        for key, obj in self.__objects.items():
            if cls is None or isinstance(obj, cls):
                result[key] = obj
        return result

    def new(self, obj):
        """Adds a new object to storage
        Args:
            obj: The object to add
        """
        if obj:
            key = f"{type(obj).__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes objects to the JSON file"""
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(
                {key: value.to_dict() for key, value in self.__objects.items()},
                f
            )

    def reload(self):
        """Deserializes objects from the JSON file"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for key, val in data.items():
                    cls = val.pop("__class__")
                    self.__objects[key] = globals()[cls](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Removes an object from storage
        Args:
            obj: The object to remove
        """
        if obj:
            key = f"{type(obj).__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Reloads objects from the JSON file"""
        self.reload()
