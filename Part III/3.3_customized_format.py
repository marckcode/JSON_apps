from jsonschema import validate, ValidationError, Draft202012Validator
import re

schema = {
    "type": "object",
    "properties": {
        "address": {
            "type": "object",
            "properties": {
                "zip_code": {
                    "type": "string",
                    "format": "us-zip-code"
                }
            },
            "required": ["zip_code"]
        }
    },
    "required": ["address"]
}

document = {
    "address": {
        "zip_code": "12345ANDY"
    }
}

try:
    validate(document, schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
    print("The document is valid againt the schema.")
except ValidationError as e:
    print(f"The document is not valid against the schema: {e}")
    
    
# Function for validation logic
def is_us_zip_code(instance):
    if not re.match(r"^\d{5}(-\d{4})?$", instance):
        return False
    
    return True

# register validation function
Draft202012Validator.FORMAT_CHECKER.checks("us-zip-code")(is_us_zip_code)

try:
    validate(document, schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
    print("The document is valid againt the schema.")
except ValidationError as e:
    print(f"The document is not valid against the schema: {e}")