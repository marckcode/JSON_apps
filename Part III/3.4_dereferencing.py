# 3 different schemas that relate each other
from jsonschema import validate, ValidationError, Draft202012Validator
from referencing import Registry, Resource

address_subschema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://somedomain.xyz/schemas/address.json",
    "type": "object",
    "properties": {
        "street": {"type": "string"},
        "city": {"type": "string"},
        "state": {"type": "string"}
    },
    "required": ["street", "city", "state"]
}

person_subschema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://somedomain.xyz/schemas/person.json",
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "address": {"$ref": "https://somedomain.xyz/schemas/address.json"}
    },
    "required": ["name", "age", "address"]
}

main_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://somedomain.xyz/schemas/main.json",
    "type": "object",
    "properties": {
        "person": {"$ref": "https://somedomain.xyz/schemas/person.json"},
        "spouse": {"$ref": "https://somedomain.xyz/schemas/person.json"},
        "isMarried": {"type": "boolean"}
    },
    "required": ["person", "isMarried"],
    "if": {
        "properties": {"isMarried": {"const": True}}
    },
    "then": {
        "required": ["person", "spouse"]
    }
}


document = {
    "person": {
        "name": "John Doe",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "Anystate"
        }
    },
    "spouse": {
        "name": "Jane Doe",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "Anystate"
        }
    },
    "isMarried": True
}

# try:
#     validate(document, main_schema)
#     print("The document is valid againt the schema.")
# except ValidationError as e:
#     print(f"The document is not valid against the schema: {e}")


## Create new instance of Registry
registry = Registry().with_resources(
    [
        ("https://somedomain.xyz/schemas/address.json", Resource.from_contents(address_subschema)),
        ("https://somedomain.xyz/schemas/person.json", Resource.from_contents(person_subschema))
    ]
)

# The validator know what to reference
validator = Draft202012Validator(
    main_schema,
    registry=registry
)

try:
    validator.validate(document)
    print("The document is valid againt the schema.")
except ValidationError as e:
    print(f"The document is not valid against the schema: {e}")