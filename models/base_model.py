#!/usr/bin/python3
from datetime import datetime
import uuid
import models
"""
This module contains a class BaseModel that defines\
        all common attributes /methods for other classes:
"""


class BaseModel():
    """
    This class contains three public instance attributes\
            id | created_at | updated_at
    This class also contains two publis instance methods\
            save | to_dict
    """
    def __init__(self, *args, **kwargs):
        """
        this initialization method creates a unique id\
                and creates a time instance
        """
        if bool(kwargs) is False:
            self.id = uuid.uuid4()
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ["__class__"]:
                    pass
                elif key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                    self.__setattr__(key, value)
                else:
                    self.__setattr__(key, value)

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
        models.storage.save()

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
