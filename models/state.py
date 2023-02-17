#!/usr/bin/python3
"""
Defines the State class
"""
import models
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represent a state

    Attributes:
        name (str): The name of the state
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
