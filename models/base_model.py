#!/usr/bin/env python3
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.save()
    
    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        return datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

    def to_dict(self):
        # setattr(BaseModel, '__class__', self.__class__.__name__)
        self.__dict__['__class__'] = str(self.__class__.__name__)
        return (self.__dict__)



b = BaseModel()
# print("strrrrrrrrrrrrrr")
# print(b.__str__())

# print("dicctttttttttttt")
# print(b.__dict__)

# print("to00000000000 dict")

b.name = "My First Model"
b.my_number = 89

print("This is my Object")
print(b)

b.to_dict()
my_model_json = b.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))