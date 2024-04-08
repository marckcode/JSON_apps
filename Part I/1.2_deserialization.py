import json

json_data = '{"name": "John Doe", "age": 30, "city": "New York"}'

person = json.loads(json_data)

print(person)
print(type(person))

print(person["name"])

## DESERIALIZATION
# JSON format string into a python dict.
with open("create_person.json", "r") as file:
    person_from_disk = json.load(file)
    
print(person_from_disk)
print(type(person_from_disk))