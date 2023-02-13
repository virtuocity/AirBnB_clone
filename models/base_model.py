#!/usr/bin/python3
"""AirBnB clone - the console Base class"""
from uuid import uuid4
from datetime import datetime as date


class BaseModel:
    """class base model"""

    def __init__(self, *args, **kwargs):
        """
            instantiation of new BaseModel object
        """
        if kwargs:
            self.__set_attribs(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = date.utcnow()

    def __set_attribs(self, attrib_dict):
        """
            private method: converts attr_dict values to python class attributes
        """
        if 'id' not in attrib_dict:
            attrib_dict['id'] = str(uuid4())
        if 'created_at' not in attrib_dict:
            attrib_dict['created_at'] = date.utcnow()
        elif not isinstance(attrib_dict['created_at'], date):
            attrib_dict['created_at'] = date.strptime(
                attrib_dict['created_at'], "%Y-%m-%d %H:%M:%S.%f"
            )
        if 'updated_at' not in attrib_dict:
            attrib_dict['updated_at'] = date.utcnow()
        elif not isinstance(attrib_dict['updated_at'], date):
            attrib_dict['updated_at'] = date.strptime(
                attrib_dict['updated_at'], "%Y-%m-%d %H:%M:%S.%f"
            )
        for attr, val in attrib_dict.items():
            setattr(self, attr, val)

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
        dict["__class"] = self.__class__
        return dict

    def save(self):
        """ Update updated at time"""
        self.updated_at = date.utcnow()
