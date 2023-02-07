#!/usr/bin/python3
"""
class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances
"""
import json

class FileStorage():
    """
    """
    __file_path = "Air.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return __objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, "a+", encoding="utf-8") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
        
