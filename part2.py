import json
import urllib.request
import time

# Read the JSON file created in Part 1
with open("state_capitals.json", "r") as f:
    state_capitals = json.load(f)

results = []

# Loop through each state capital and get coordinates
for item in state_capitals:
    address = item["address"]
    
    # Encode the address for use in URL
    encoded_address = urllib.parse.quote(address)
    url = f"https://nominatim.openstreetmap.org/search?q={encoded_address}&format=json&limit=1"
    
    # Send request to geocoding API
    req = urllib.request.Request(url, headers={"User-Agent": "state-capitals-project"})
    
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            
        if data:
            lat = float(data[0]["lat"])
            lon = float(data[0]["lon"])
            print(f"{item['state']}: {lat}, {lon}")
        else:
            lat = None
            lon = None
            print(f"{item['state']}: not found")
            
    except Exception as e:
        lat = None
        lon = None
        print(f"{item['state']}: error - {e}")
    
    results.append({
        "state": item["state"],
        "capital": item["capital"],
        "address": item["address"],
        "latitude": lat,
        "longitude": lon
    })
    
    # Wait 1 second between requests to be polite to the API
    time.sleep(1)

# Save results to a new JSON file
with open("state_capitals_with_coordinates.json", "w") as f:
    json.dump(results, f, indent=4)

print("\nDone! File saved as state_capitals_with_coordinates.json")
print(f"Total states processed: {len(results)}")