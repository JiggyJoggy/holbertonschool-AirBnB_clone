#!/usr/bin/python3
"""File storage module"""
import json
from models.base_model import BaseModel


class FileStorage():
    """File storage class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
    
    def save(self):
        """Placeholder"""
        pass