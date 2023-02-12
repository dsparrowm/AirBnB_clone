#!/usr/bin/python3
"""
This module contains a class BaseModel that defines\
        all common attributes/methods for other classes:
"""
import uuid
from models import storage
from datetime import datetime


class BaseModel():
    """
    This class contains three public instance attributes
            id | created_at | updated_at
    This class also contains two publis instance methods
            save | to_dict
    """
    def __init__(self, *args, **kwargs):
        """
        this initialization method creates a unique id\
                and creates a time instance
        """
        if kwargs:
            for key in kwargs:
                if key == 'created_at':
                    self.__dict__['created_at'] = datetime.strptime(
                            kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.__dict__['updated_at'] = datetime.strptime(
                            kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = uuid.uuid4()
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        returns a representation of the class like this\
                [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute\
                updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all \
                keys/values of __dict__ of the instance:
        """
        temp = self.__dict__.copy()
        temp["id"] = str(self.id)
        temp["__class__"] = self.__class__.__name__
        temp["created_at"] = self.created_at.isoformat()
        temp["updated_at"] = self.created_at.isoformat()
        return temp
