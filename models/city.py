#!/usr/bin/python3
""" This module contains a class City that inherits from BaseModel """


from models.base_model import BaseModel


class City(BaseModel):
    """ class City that contains public attributes:
        state_id and name (both empty strings) """
    state_id = ""
    name = ""
