#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj

    def save(self):
        with open(self.__file_path, 'w+') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                dict = json.loads(f.read())
                for value in dict.values():
                    cl = value["__class__"]
                    self.new(eval(cl)(**value))
        except Exception:
            pass
