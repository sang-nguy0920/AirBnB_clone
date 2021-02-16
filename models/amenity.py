#!/usr/bin/python3
""" This module contains a class Amenity that inherits from BaseModel """


from models.base_model import BaseModel
from models.engine import file_storage


class Amenity(BaseModel):
    """ class Amenity that contains the public attribute:
        name (an empty string) """
    name = ""
