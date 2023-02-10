#!/usr/bin/python3
"""AirBnB clone - the console Base class"""
from uuid import uuid4
from datetime import datetime as date
import json


class BaseModel:
    """class base model"""
    def __init__(self, my_number, name, id, created_at, updated_at):
        self.my_number = my_number
        self.name = name
        self.id = id
        self.created_at = created_at
        self.update_at = updated_at
    
    def __str__(self):
        print("{} {} {}".format((self.__class__, self.id, self.to_dict)))
    
    def to_dict(self):
        dict = {}
        for key, val in self.__dict__.items():
            dict[key] = val
        return dict
    
    @property
    def save(self):
        """ Update updated at time"""
        return self.update_at


    