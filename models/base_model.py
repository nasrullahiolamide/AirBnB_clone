#!/usr/bin/env python3
import uuid
from datetime import datetime
import models as models

"""
Class BaseModel
"""
class BaseModel:
    def __init__(self, *args, **kwargs):
        """"
        Initialization function
        """

        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    pass
                elif k in ["created_at", "updated_at"]:
                    setattr(self, k, datetime.strptime(
                        v, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        String representation of the object
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """
        Function to update the object
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:
        by using self.__dict__, only instance attributes set will be returned
        a key __class__ must be added to this dictionary with the class name of the object
        created_at and updated_at must be converted to string object in ISO format
        """
        # setattr(BaseModel, '__class__', self.__class__.__name__)
        newDict = {}
        newDict['__class__'] = str(self.__class__.__name__)

        for key, value in self.__dict__.items():

            if key in ['updated_at', 'created_at']:
                newDict[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                newDict[key] = value

        return (newDict)
