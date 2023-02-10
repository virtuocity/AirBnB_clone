#!/usr/bin/python3
"""AirBnB clone - the console Base class"""
from uuid import uuid4
from datetime import datetime as date
import json


class BaseModel:
    """class base model"""
    def __init__(self, id, created_at, update_at):
        self.id = id
        self.created_at = created_at
        self.update_at = update_at
    
    def __str__(self):
        return "" % (self.__class__, self.id, self.__dict__)
    
    def to_dict(self):
        dict = {}
        for key, val in self.__dict__.items():
            dict[key] = val
        return dict

    