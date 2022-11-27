#!/usr/bin/python3

import json
from models.base_model import BaseModel

"""Class FileStorage"""

class FileStorage:

    __file_path = "file.json"
    __objects = {}
    classObj = {"BaseModel": BaseModel}

    def all(self):
        """ """
        return self.__objects
        
    def new(self, obj):

        key = "{}.{}".format(obj.__class__.__name__, obj.id)

        self.__objects[key] = obj

    def save(self):
        """Serilize json file"""
        serializeDict = {}

        for key, value in self.__objects.items():
            serializeDict[key] = value.to_dict()

        with open(self.__file_path, 'w') as serializer:
            stringObj = json.dumps(serializeDict)
            serializer.write(stringObj)
            

    def reload(self):
        try:
            with open(self.__file_path) as deserializer:
                deserialize = json.load(deserializer)

            deserializeDict = {}
            for k, v in deserialize.items():
                classKey = k.split(".")[0]
                deserializeDict[k] = BaseModel(**v)
            
            self.__objects = deserializeDict
        except FileNotFoundError:
            pass


    