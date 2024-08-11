import json

# Python dictionary
data = {
    "name": "John",
    "age": 30,
    "married": True,
    "children": ["Ann", "Billy"],
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# Convert to JSON string
json_string = json.dumps(data, indent=4)
print("JSON String:")
print(json_string)

# Write JSON to a file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

# Read JSON from a file
with open('data.json', 'r') as json_file:
    data_from_file = json.load(json_file)

print("\nData Loaded from File:")
print(data_from_file)

# Convert JSON string back to Python object
python_data = json.loads(json_string)
print("\nPython Data:")
print(python_data)
