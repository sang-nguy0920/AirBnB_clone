#!/usr/bin/python3
""" This module contains a class Review that inherits from BaseModel """


from models.base_model import BaseModel
from models.engine import file_storage


class Review(BaseModel):
    """ class Review that contains the public attributes:
        place_id, user_id and text (all empty strings) """
    place_id = ""  # task says will be: Place.id :later
    user_id = ""  # task says will be: User.id :later
    text = ""
