from jsonschema import validate, ValidationError, Draft202012Validator

# the validation format is not enforced by default
document = {
    "date": "2024 07" # not valid
}

schema = {
    "type": "object",
    "properties": {
        "date": {
            "type": "string",
            "format": "date"
        }
    }
}

# VALID
try:
    validate(document, schema)
    print("The document is valid againt the schema.")
except ValidationError as e:
    print(f"The document is not valid against the schema: {e}")
    
print(Draft202012Validator.FORMAT_CHECKER) # 'date' is the first to validate

# INVALID
try:
    validate(document, schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
    print("The document is valid againt the schema.")
except ValidationError as e:
    print(f"The document is not valid against the schema: {e}")