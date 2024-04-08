import jsondiff
from jsondiff import patch

json1 = {
    "name": "John", 
    "age": 30, 
    "city": "New York",
    "hobbies": ["reading", "cooking"], 
    "isMarried": True
}

json2 = {
    "name": "John", 
    "age": 28, 
    "city": "Los Angeles",
    "hobbies": ["cooking", "reading"]
}

# print(jsondiff.diff(json1, json2))
# print(jsondiff.diff(json1, json2, syntax="explicit"))
# print(jsondiff.diff(json1, json2, syntax="symmetric"))
# print(jsondiff.diff(json1, json2, syntax="compact"))
diffs = print(jsondiff.diff(json1, json2))
# print(diffs)

# recreate json2 from json1
print(patch(json1, json2))

print(patch(json2, diffs))