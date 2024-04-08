from jsonpath_ng.ext import parse # importing from 'extensions' module

document = {
    "people": [
        {"name": "Alice"  , "age": 28, "city": "New York"},
        {"name": "Bob"    , "age": 35, "city": "Los Angeles"},
        {"name": "Charlie", "age": 22, "city": "Austin"},
        {"name": "Diana"  , "age": 30, "city": "Houston"},
        {"name": "Edward" , "age": 40, "city": "Miami"},
        {"name": "Fiona"  , "age": 25, "city": "San Francisco"},
        {"name": "George" , "age": 32, "city": "Seattle"},
        {"name": "Helen"  , "age": 27, "city": "Boston"},
        {"name": "Ivan"   , "age": 38, "city": "Denver"},
        {"name": "Jasmine", "age": 23, "city": "Austin"},
    ]
}

# 1: all ppl older than 30
try:
    expr = parse("$.people[0:3]")
    for match in expr.find(document):
        print(match.value)
except Exception as e:
    print(f"Error: {str(e)}")

print("\n")

# 2: 3 first ppl
try:
    expr = parse("$.people[?(@.age > 30)]")
    for match in expr.find(document):
        print(match.value)
except Exception as e:
    print(f"Error: {str(e)}")
    
print("\n")

# 3: all ppl that lives in Austin
try:
    expr = parse("$.people[?(@.city == 'Austin')]")
    for match in expr.find(document):
        print(match.value)
except Exception as e:
    print(f"Error: {str(e)}")