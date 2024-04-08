from jsonpath_ng import parse

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

# $.spouse.address.zipcode --> 67890
result = parse("$.spouse.address.zipcode").find(document)
print(result[0].value)

result = parse("$.person.name").find(document)
print(result[0].value)

result = parse("$.spouse.age").find(document)
print(result[0].value)