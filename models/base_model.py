#!usr/bin/python3
from datetime import datetime
import uuid
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
    def __init__(self):
        """
        this initialization method creates a unique id\
                and creates a time instance
        """
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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

    def to_dict(self):
        """
        returns a dictionary containing all \
                keys/values of __dict__ of the instance:
        """
        temp = self.__dict__
        temp["id"] = str(self.id)
        temp["__class__"] = self.__class__.__name__
        temp["created_at"] = self.created_at.isoformat()
        temp["updated_at"] = self.updated_at.isoformat()
        return temp
