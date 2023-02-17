#!/usr/bin/python3
"""
Module for Amenity class
"""
import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Custom amenity class

    Attributes:
        name(str): amenity name
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
