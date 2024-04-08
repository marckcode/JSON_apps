import json
import requests
from jsonschema import Draft202012Validator

URL_CONSTANT = "https://www.andybek.com/api/data/stock-tickers"

response = requests.get(URL_CONSTANT)
data = response.json()
# print(data)

# define the schema
schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "ticker": {"type": "string"},
            "price": {"type": "number"},
            "currency": {"type": "string", "enum": ["USD", "CAD"]}
        },
        "required": ["ticker", "price", "currency"],
        "additionalProperties": False
    }
}

# validate the data against the defined schema
validator = Draft202012Validator(schema)

invalid_records = []

for index, item in enumerate(data):
    # 0, first item
    # 1. second item ....
    
    # do validation
    for error in validator.iter_errors([item]):
        invalid_records.append({
            "index": index, 
            "record": error.instance,
            "reason": error.message
        })
        
print("Invalid Records: ")
for record in invalid_records:
    print(f"Record ${record['index']+1} is invalid")
    print("Record: ")
    print(json.dumps(record['record'], indent=2))
    print("Reason: ", record["reason"])
    print("\n" + "=" * 40 + "\n")