#!/usr/bin/python3
""" This module contains a class FileStorage  that serializes instances to a...
    ...JSON file and deserializes JSON file to instances """


import json
import uuid
from datetime import datetime
import models
time = "%Y-%m-%dT%H:%M:%S.%f"


class FileStorage():
    """ FileStorage Class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ all method:  returns the dictionary __objects """
        return (self.__objects)

    def new(self, obj):
        """ new method: sets __objects with a key id """
        if obj:
            var_id = "{}, {}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[var_id] = obj

    def save(self):
        """ save method: serializes __objects to the JSON file """
        s_dict = {} 
        for var_id, var_obj in FileStorage.__objects.items():
            s_dict[var_id] = var_obj.to_dict()
        
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(s_dict, f)

    def reload(self):
        """ reload method: deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                obj = json.load(f)
            for key, value in obj.items():
                name = models.ourclasses[value['__class__']](**value)
                self.__objects[key] = name
        except FileNotFoundError:
            pass
