import requests

url = "https://www.andybek.com/api/data/persons"

response = requests.get(url) # encoded
data =  response.json()

print(data[9]) # deserialized into python objects <list>
print(type(data), type(data[9]))
