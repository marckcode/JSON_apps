import difflib
import json

text1 = "apple banana cherry"
text2 = "apple cherry date"

differ = difflib.Differ()

# + : unique to the second string
# - : unique to the first  string
print(list(differ.compare(text1.split(), text2.split())))

json1 = {"name": "John", "age": 30, "city": "New York",
         "hobbies": ["reading", "cooking"], "isMarried": True}
json2 = {"name": "John", "age": 28, "city": "Los Angeles"}

json1_str = json.dumps(json1, indent=2)
json2_str = json.dumps(json2, indent=2)

differ = difflib.Differ()
diff = list(
    differ.compare(
        json1_str.splitlines(),
        json2_str.splitlines()
    )
)
print("\n".join(diff))

