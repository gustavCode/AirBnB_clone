#!/usr/bin/python3
"""
Defines the base model for classes
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """A model class that defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initialize id, created_at, and updated_at
        attributes
        """
        if (len(kwargs) != 0):
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.now()
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".
    format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        self.created_at = datetime.isoformat(self.created_at)
        self.updated_at = datetime.isoformat(self.updated_at)
        a_dict = self.__dict__
        a_dict["__class__"] = __class__.__name__
        return a_dict
