# State Capitals Project

## Overview
A two-part Python project that collects all 50 US state capital addresses
and retrieves their GPS coordinates using a geocoding API.

## Background
Geographic data is foundational to data science workflows. This project
demonstrates how to structure, store, and enrich location-based data
using Python and a public geocoding API.

## Data

| Source | File | Coverage |
|--------|------|----------|
| Manually compiled | `state_capitals.json` | All 50 US states |
| Nominatim Geocoding API | `state_capitals_with_coordinates.json` | 47 of 50 states geocoded |

Key fields per state:
- State name
- Capital city
- Official address
- **Latitude and Longitude** ← primary output target

## Repository Structure
├── part1.py                               # Generates state capitals JSON
├── part2.py                               # Adds coordinates via geocoding API
├── state_capitals.json                    # Output from Part 1
└── state_capitals_with_coordinates.json   # Output from Part 2
## Setup

### Prerequisites
- Python 3.x (no third-party packages required)

### Clone the repository
```bash
git clone https://github.com/RossJiao/state-capitals-project.git
cd state-capitals-project
```

## Run

### Step 1 — Generate address data
```bash
python3 part1.py
```
Output: `state_capitals.json`

### Step 2 — Add GPS coordinates
```bash
python3 part2.py
```
Output: `state_capitals_with_coordinates.json`

## Sample Output
```json
{
    "state": "California",
    "capital": "Sacramento",
    "address": "1315 10th St, Sacramento, CA 95814",
    "latitude": 38.5766749,
    "longitude": -121.4937139
}
```

## Results
- 47 out of 50 states successfully geocoded
- Minnesota, Ohio, and Tennessee returned no results from the API

## Limitations
- **Missing states (n=3):** Minnesota, Ohio, and Tennessee were not
  found by the Nominatim API, likely due to address formatting issues
- **No external driver:** The coordinates are sourced from a single
  free API and have not been cross-validated against other sources

## Tools Used
- Python 3 standard library only
- `json` — read and write JSON files
- `urllib.request` — send HTTP requests
- `time` — rate limiting between API calls
- [Nominatim API](https://nominatim.openstreetmap.org/) — open-source geocoding by OpenStreetMap
