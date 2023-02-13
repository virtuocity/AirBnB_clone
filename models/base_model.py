from uuid import uuid4
from datetime import datetime as date


class BaseModel:
    """class base model"""

    def __init__(self, my_number=0, name="", updated_at=date.utcnow(), id=str(uuid4()),
                 created_at=date.utcnow()):
        self.my_number = my_number
        self.name = name
        self.updated_at = updated_at
        self.id = id
        self.created_at = created_at

    def __str__(self):
        """
            returns informal string representation of object instance
        """
        class_name = type(self).__name__
        return '[{}] ({}) {}'.format(class_name, self.id, self.__dict__)

    def insert_at_nth_position(dictitonary, n, key, value):
        if n < 0 > len(dictitonary):
            raise ValueError("Index out of range")
        items = list(dictitonary.items())
        items.insert(n, (key, value))
        return dict(items)

    def to_dict(self):
        """Dict representation of object"""
        dict = {}
        for key, val in self.__dict__.items():
            if key is "updated_at":
                dict["updated_at"] = date.isoformat(val)
            elif key is "created_at":
                dict["created_at"] = date.isoformat(val)
            else:
                dict[key] = val
        dict["__class__"] = self.__class__.__name__
        return dict

    def save(self):
        """ Update updated at time"""
        self.updated_at = date.utcnow()
