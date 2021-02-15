#!/usr/bin/python3
""" This module contains a class State that inherits from BaseModel """


from models.base_model import BaseModel
from models.engine import file_storage

class State(BaseModel):
    """ class State that contains the public attribute:
        name (an empty string) """
    name = ""
