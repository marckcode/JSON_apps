from deepdiff import DeepDiff

json1 = {
    "name": "John", 
    "age": 30, 
    "city": "New York",
    "hobbies": ["reading", "cooking"], 
    "isMarried": True
}

json2 = {
    "age": 28, 
    "name": "John", 
    "city": "Los Angeles",
    "hobbies": ["cooking", "reading"]
}

diff = DeepDiff(json1, json2)
print(diff)
print("\n")
print(diff.pretty())

print("\n")
diff = DeepDiff(json1, json2, ignore_order=True)
print(diff.pretty())