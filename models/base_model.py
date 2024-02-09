#!/usr/bin/python3
"""A base model that all other models (classes) will inherit from"""


from uuid import uuid4
import datetime
from models import storage
class BaseModel:
    """Base model for other models"""
    def __init__(self, *args, **kwargs):
        """Create an instance"""
        if kwargs:
            # NOTE: I may simply do,  <self.__dict__ = kwargs> and then
            # delete from __dict__ the attribute "__class__" if any.
            # I guess this may be ok

            for key, value in kwargs.items():
                if not key == "__class__":
                    self.__setattr__(key, value)

            if hasattr(self, "created_at"):
                self.created_at = datetime.datetime.strptime(\
                    self.created_at, "%Y-%m-%dT%H:%M:%S.%f")

            if hasattr(self, "updated_at"):
                self.updated_at = datetime.datetime.strptime(\
                    self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Define the string representation of an instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute to the current time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Make a dictionary of the attributes of the instance

            - Add the __class__ attribute, holding class name
            - change the created_at and updated_at object into a string
        """
        attributes = {k:y for k, y in self.__dict__.items()}
        attributes["__class__"] = self.__class__.__name__
        attributes["created_at"] = attributes["created_at"].isoformat()
        attributes["updated_at"] = attributes["updated_at"].isoformat()

        return attributes
