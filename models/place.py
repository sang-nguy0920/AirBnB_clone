#!/usr/bin/python3
""" This module contains a class Place that inherits from BaseModel """


from models.base_model import BaseModel
from models.engine import file_storage

class Place(BaseModel):
    """ class Place that contains the public attributes:
        city_id (empty str), user_id (empty str), name (empty str),
        description (empty str), number_rooms (integer - 0),
        number_bathrooms (integer - 0), max_guest (integer - 0),
        price_by_night (integer - 0), latitude (float - 0.0),
        longitude (float - 0.0), amenity_ids (list of strings - empty list)
    """
    city_id = ""  # task says will be: City.id :later
    user_id = ""  # task says will be: User.id :later
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
