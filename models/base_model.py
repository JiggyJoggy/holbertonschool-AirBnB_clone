#!/usr/bin/python3
"""Base module"""
import uuid
import datetime


class BaseModel():
    """Defines all common attributes/methods for other classes"""
    def __init__(self, ):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """String representation"""
        print(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values"""
        dictionary = self.__dict__.copy()
        dictionary.update({
            'created_at': datetime.isoformat(self.created_at),
            '__class__': self.__class__.__name__,
            'updated_at': datetime.isoformat(self.updated_at)
        })
        return dictionary
