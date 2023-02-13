#!/usr/bin/python3
"""Persistent file storage for class instance dictionary"""
from models import base_model
import json
from datetime import datetime as datetime

strptime = datetime.strptime
to_json = base_model.BaseModel.to_json

class FileStorage:
    """Data persistence in a file"""
    cls_dict = {'BaseModel': base_model.BaseModel}
    """
    cls_dict is a dictionary
    keys: Class Names
    values: Class type (used for instantiation)
    """
    __file_path = './dev/file.json'
    __objects = {}

    def all(self, cls=None):
        """ returns the dictionary __objects"""
        if cls is not None:
            new_objs = {}
            for clsid, obj in FileStorage.__objects.items():
                if type(obj).__name__ == cls:
                    new_objs[clsid] = obj
            return new_objs
        else:
            return FileStorage.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key < obj class name > .id"""
        basem_id = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[basem_id] = obj

    def save(self):
        """serializes __objects to the JSON file(path: __file_path)"""
        fname = FileStorage.__file_path
        storage_d = {}
        for basem_id, basem_obj in FileStorage.__objects.items():
            storage_d[basem_id] = basem_obj.to_json(saving_file_storage=True)
        with open(fname, mode='w', encoding='utf-8') as f:
            json.dump(storage_d, f)

    
    def reload(self):
        """deserializes the JSON file to __objects"""
        filename = FileStorage.__file_path
        FileStorage.__objects = {}
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                new_objs = json.load(f)
        except:
            return
        for o_id, d in new_objs.items():
            k_cls = d['__class__']
            FileStorage.__objects[o_id] = FileStorage.CNC[k_cls](**d)
    

