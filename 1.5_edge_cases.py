import json
from json import JSONEncoder
from datetime import datetime, date

class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date) or isinstance(obj, datetime):
            return obj.isoformat()
        
        return super().default(obj)
        

now = datetime.now()
print(now)

dog_data = {
    "name": "Spot",
    "breed": "Dalmatian",
    "birthday": date(2019, 5, 12)
}

print(dog_data)
print(json.dumps(dog_data, cls=CustomEncoder)) 

