import json

capitals = [
    {
        "state": "Iowa",
        "capital": "Des Moines",
        "address": "1007 E Grand Ave, Des Moines, IA 50319"
    },
    {
        "state": "California",
        "capital": "Sacramento",
        "address": "1315 10th St, Sacramento, CA 95814"
    }
]

with open('capitals.json', 'w') as f:
    json.dump(capitals, f, indent=2)

print("capitals.json created")
print("File content:")
print(json.dumps(capitals, indent=2))