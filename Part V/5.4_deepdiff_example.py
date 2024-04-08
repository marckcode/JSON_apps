from deepdiff import DeepDiff

profile1 = {
    "user": {
        "name": "Alice",
        "details": {
            "age": 30,
            "address": {"street": "123 Main St", "city": "Townsville"}
        },
    }
}

profile2 = {
    "user": {
        "name": "Alice",
        "details": {
            "age": 31,
            "address": {"street": "123 Main St", "city": "VillageTown"}
        },
    }
}

diff = DeepDiff(profile1, profile2)
print(diff.pretty())

print("\n")
diff = DeepDiff(profile1, profile2, exclude_paths={"root['user']['details']['age']"})
print(diff.pretty())

print("\n")
diff = DeepDiff(profile1, profile2, include_paths={"root['user']['details']['age']"})
print(diff.pretty())