import json

person_data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

print(type(person_data))
print(json.dumps(person_data))
print(json.dumps(person_data, indent=4))

### SERIALIZATION
# Serialize python dictionary into a JSON format string
# & storing the resulting ouput in a file
with open("create_person.json", "w") as file: 
    print(json.dump(person_data, file, indent=4))
