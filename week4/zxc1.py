import json

person = {
    "name": "Ali",
    "age": 18,
    "grades": [90, 85, 88]
}

json_text = json.dumps(person)
print(json_text)

new_person = json.loads(json_text)
print(new_person["grades"])