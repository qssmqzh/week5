import json

data = {
    "name": "Ergali",
    "age": 20
}

json_string = json.dumps(data)

print(json_string)