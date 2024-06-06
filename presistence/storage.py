#!/usr/bin/env python3
"""
This module contains classes representing file storage.
"""
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.id] = obj

    def save(self):
        obj_dict = {obj.id: obj.to_dict() for obj in self.__objects.values()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for obj in obj_dict.values():
                    class_name = obj.pop("__class__")
                    self.__objects[obj["id"]] = eval(class_name)(**obj)
        except FileNotFoundError:
            pass
