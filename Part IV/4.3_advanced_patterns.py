from jsonpath_ng.ext import parse

document = {
    "person": {
        "name": "Alice Johnson",
        "age": 28,
        "gender": "female",
        "contact": {
            "email": "alice@example.com",
            "phone": "555-123-4567"
        },
        "address": {
            "street": "456 Oak Avenue",
            "city": "Somewhereville",
            "zipcode": "12345",
            "country": "USA"
        },
        "interests": ["reading", "traveling", "gardening"]
    },
    "spouse": {
        "name": "Bob Johnson",
        "age": 32,
        "gender": "male",
        "contact": {"email": "bob@example.com", "phone": "555-987-6543"},
        "address": {
            "street": "789 Pine Street",
            "city": "Anywhere",
            "zipcode": "67890",
            "country": "USA"
        },
        "interests": ["cooking", "photography", "music"]
    }
}

# 0. Define a reusable helper that parses and evaluates and expression against a document
def evaluation_parser(jsonpath_str, data_dict):
    try:
        expr = parse(jsonpath_str)
        matches = expr.find(data_dict)
        
        if matches:
            for match in matches:
                print(match.value)
        else:
            print("No matches found.")
    except Exception as e:
        print(f"Error: {str(e)}")
        
evaluation_parser("$.spouse.name", document)

print("\n")
# 1. Select the email and phone properties for the person object
evaluation_parser("$.person.contact['email', 'phone']", document)

print("\n")
# 2. Select all interests ending with "ing"
# evaluation_parser("$..interests", document)
evaluation_parser("$..interests[?(@ =~ '.*ing$')]", document) # regular expressions