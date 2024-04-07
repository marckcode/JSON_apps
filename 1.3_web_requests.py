import urllib.request
import json

url = "https://www.andybek.com/api/data/persons"

with urllib.request.urlopen(url) as response:
    # decode the bytes into utf-8 encode string (unicode)
    response_data = response.read().decode("utf-8")
    
print(response_data)
print(type(response_data))

json_data = json.loads(response_data) # deserialized after the API call
print(json_data)
print(type(json_data), type(json_data[0]))