#!/usr/bin/python3
"""AirBnB clone - the console Base class"""
from uuid import uuid4
from datetime import datetime as date


class BaseModel:
    """class base model"""

    def __init__(self, my_number=0, name="", id=str(uuid4()),
                 created_at=date.utcnow(), updated_at=str(date.utcnow())):
        self.my_number = my_number
        self.name = name
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        """
            returns informal string representation of object instance
        """
        class_name = type(self).__name__
        return '[{}] ({}) {}'.format(class_name, self.id, self.__dict__)

    def to_dict(self):
        """Dict representation of object"""
        dict = {}
        for key, val in self.__dict__.items():
            dict[key] = val
        return dict

    def save(self):
        """ Update updated at time"""
        self.updated_at = date.utcnow()
