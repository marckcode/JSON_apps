# 1. Introduction to JSON
- Javascript Object Notation (JSON)
- Lightweight data-interchange format
- Easy to read and write
- Language-independent

## Basic Structure
- Two universal data structures
- A collection of name/value pairs (object)
- An ordered list of values (array)

## JSON Syntax
- Squared brackets \[] hold arrays
- Curly braces \{} hold objects
- Data is in name/value pairs 
- Data is separated by commas

## Why is so popular?
- Configuration
- Serializing structured data
- Storing and exchanging data in NoSQL databases
- Logging and debugging 
- Human-readable and writable

## Core Data types
- Object
- Array
- String
- Number (Int, Float, Double, etc)
- Boolean
- Null

## Commom Data shapes
- Basic key/name entity
- List of entities
- Complex/referential entity


## Difference between Python Dict & JSON

| FEATURE         | JSON                 | Python DICT |
| :--------:      | :-------:            | :-------: |
| Purpose         | Data Exchange        | In memory DS    |
| Data Types      | Limited set of DT    | Wide range of DT    |
| Keys            | Strings Only         | Any immutable, hashable type    |
| Ordering        | Order not guaranteed | Order of keys guaranteed    |
| Absence of val  | Null                 | None    |
| Booleans        | True, False          | True, False    |
| Comments        | Not supported        | Supported    |
| Trailing commas | Not supported        | Supported    |

## The JSON Module & Serialization

- Serialization: Python Object -> JSON
- Deserialization: JSON -> Python Object

## Web Requests & APIs

- HTTP is used for transmitting requests and information between servers and browsers.
- Client makes the request, the server responds with some data.
- A Better Alternative: The 'Request' Library

## Edge Cases in Serialization

- Limitations to be aware of:
  - Some classes or objects cannot be deserialized (extent serialization for specific types)
  - Serializing User-Defined Classes (subclassing)


# Task 1: JSON Data Transformation

- Retrieve and process JSON data from a URL containing information about books. Follow the steps:
    - Use the provided URL: <a>https://www.andybek.com/api/data/books</a> to fetch all the books.
    - Save the raw JSON data to a file named "books-original.json".
    - Deserialize the JSON data and remove the "ranks" and "release dates" from each book entry.
    - Save the modified books data to a new file named "books-cleaned.json".

# 2. Schemas & Instance Validation

- Schema is a formal description of the structure of a dataset (types, constraints, relationship between attributes).
- Validates that data is consistant.
- The dominant schema standard in JSON is <a>https://json-schema.org</a>

## Schema Construction
- Interactive definition of JSON schema: <a>https://www.jsonschemavalidator.net/</a>

## Subschemas & remote references: $ref & $defs
- $ref enables schema modularization and reusability
- $defs is the conventional named section for holding definitions in a schema
- Remote review definition: <a>https://www.andybek.com/api/data/review-schema</a>

## Applicators & advanced techniques
- Applicators allow us to apply subschemas to specific parts of the model.
- They could be used to define highly specific and conditional validation conditions.

# Task 2: Defining Polymorphic JSON Schema

- Define a schena that restrictively validates the following JSON document:
- <a>https://www.andybek.com/api/data/contentItems</a>

    - Focus on keywords like "array", "object", "type", "enum"
    - Consider using the $defs keyword to organize your schema
    - For "image/jpeg", contentEncoding: "base64" ensures image data is correctly encoded. For e.g.
      - {
        - "type": "string",
        - "contentEncoding": "base64"
      - }
  

## Crafting Customized Formats

## Dereferencing
- Define schemas more modularly, combine them by reference.
- $id is used to assign unique identifiers to schemas
- Registry: Collection of resources, where each resource is a schema or a part of schema that has a unique identifier.

# Task 3: Programmatic JSON Document Validation From API

- Inspect the following JSON document, which contains USD and CAD stock price information:
  -  <a>https://www.andybek.com/api/data/stock-tickers</a>
- Define a restrictive schema for the data that will identify records
- Using Python, read in the JSON document and validate it against the schema
- Generate a report that indicates which records are invalid, e.g.

-> Invalid Records:
- Record: ('curreny' is a required property) 
{
  "ticker": "GOOGL",
  "price": 100.2
}