import json
from geopy.geocoders import Photon
import time

with open('capitals.json', 'r') as f:
    capitals = json.load(f)

geolocator = Photon(user_agent="state_capitals_project")

for item in capitals:
    address = item['address']
    print(f"Looking up: {address}")
    
    try:
        location = geolocator.geocode(address)
        
        if location:
            item['latitude'] = location.latitude
            item['longitude'] = location.longitude
            print(f"  -> lat: {location.latitude}, lon: {location.longitude}")
        else:
            item['latitude'] = None
            item['longitude'] = None
            print(f"  -> Not found")
    except Exception as e:
        print(f"  -> Error: {e}")
        item['latitude'] = None
        item['longitude'] = None
    
    time.sleep(1)

with open('capitals_with_coords.json', 'w') as f:
    json.dump(capitals, f, indent=2)

print("capitals_with_coords.json created")