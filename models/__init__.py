#!/usr/bin/python3

from models.engine import file_storage
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity

ourclasses = {"BaseModel": BaseModel, "City": City,
                "Place": Place, "Amenity": Amenity,
                "Review": Review, "State": State,
                "User": User}

storage = file_storage.FileStorage()
storage.reload()
