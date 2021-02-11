#!/usr/bin/python3
""" This module contains a class BaseModel that defines all common...
    ...attributes/methods for other classes """


import json
import uuid
from datetime import datetime
time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        """ __init__ method:
            Args:
                self
                args: variable nonkeyworded args
                kwargs variable keyworder args
            Returns:
        """
        if kwargs:
            for key, value in kwargs.items():
                if key is not "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.now()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """ __str__ magic method:
            Args: self
            Returns: [<class name>] (<self.id>) <self.__dict__>
        """
        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))

    def save(self):
        """ save method: updates the public instance attribute updated_at
                with the current datetime
            Args: self
            Returns: updates the public instance attribute updated_at
                with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ to_dict method:
            Args: self
            Returns: returns a dictionary containing all keys/values...
            ...of __dict__ of the instance
        """
        a_dict = dict(self.__dict__)
        a_dict['__class__'] = str(type(self).__name__)
        a_dict['created_at'] = self.created_at.isoformat()
        a_dict['updated_at'] = self.updated_at.isoformat()

        return (a_dict)

