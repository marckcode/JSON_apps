import json
from json import JSONEncoder
from datetime import datetime

class Person:
    def __init__(self, name, born):
        self.name = name
        self.born = born
        
john = Person("John Doe", 1989) # Python Object

print(john.name)
print(john.born)
# print(john.__dict__)

john_json = json.dumps(john.__dict__) # serialized (Not the best way)
print(john_json)


### Create new class
class NewPerson:
    def __init__(self, name, born):
        self.name = name
        self.born = born
    
    @property
    def age(self):
        return datetime.now().year - self.born
    
marck = NewPerson("Marck Llerena", 1997)
print(marck.name)
print(marck.born)

# the dunder __dict__ just stores the instance attributes
# @property is a descriptor (resides in the class and not in the instance)
print(json.dumps(marck.__dict__))

# we define a custom serialization function
def serialize_person(obj):
    # full control over the serialization ouput
    # choose to show name & age
    if isinstance(obj, NewPerson):
        return {
            "name": obj.name,
            "age": obj.age,
        }
    
    raise TypeError('Object not serializable')

print(json.dumps(marck, default=serialize_person))