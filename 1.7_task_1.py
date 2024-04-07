import json
import requests

API_URL = "https://www.andybek.com/api/data/books"
ORIGINAL_FILE = "books-original.json"
CLEANED_FILE = "books-cleaned.json"


def fetch_and_clean():
    try: 
        response = requests.get(API_URL) # attempt to get response from url
        response.raise_for_status() # raise exception for all errors found
        data = response.json()
        
        with open(ORIGINAL_FILE, "w") as f:
            json.dump(data, f, indent=2)
        
        for book in data:
            del book["rank"]
            del book["release_date"]
            
        with open(CLEANED_FILE, "w") as f:
            json.dump(data, f, indent=2)   
        
        return f"Data named {CLEANED_FILE} stored"
         
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}") 
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON data: {e}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        
print(fetch_and_clean())
    
    