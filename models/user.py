#!/usr/bin/python3
""" This module contains a class User that inherits from BaseModel """


from models.base_model import BaseModel
from models.engine import file_storage


class User(BaseModel):
    """ class User that contains public attributes: email, password,
        first_name and last_name (all are empty strings) """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
