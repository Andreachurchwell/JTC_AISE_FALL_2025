# w2d1_users.py
import json
from datetime import date


# file handles (opening a file with open())
#  JSON read/write (json.dump() and json.load())
# basic data transformation (looping through your data to print usernames)


users = [
    {"id": 1, "username": "andrea", "email": "andrea@example.com", "is_active": True,  "created_at": str(date.today())},
    {"id": 2, "username": "brandy",  "email": "brandy@example.com",  "is_active": False, "created_at": str(date.today())},
    {"id": 3, "username": "pam",   "email": "pam@example.com",   "is_active": True,  "created_at": str(date.today())},
]

# write JSON file
with open("users.json", "w") as f:   # file handle in WRITE mode
    json.dump(users, f, indent=2)

print("✅ users.json created")


# --- READ JSON BACK INTO PYTHON ---
with open("users.json", "r") as f:       # file handle in READ mode
    loaded_users = json.load(f)          # JSON text -> Python (list of dicts)

print("✅ JSON loaded. Number of users:", len(loaded_users))
print("Usernames:")
for u in loaded_users:
    print("-", u["username"])


import csv

# --- WRITE USERS TO A CSV FILE ---
with open("users.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "username", "email", "is_active", "created_at"])
    writer.writeheader()              # write column names first
    writer.writerows(loaded_users)    # write each dictionary as a row

print("✅ users.csv created")


# --- READ CSV BACK INTO PYTHON ---
rows = []
with open("users.csv", "r", newline="") as f:
    reader = csv.DictReader(f)   # each row -> dict using the header
    for row in reader:
        rows.append(row)
print("✅ CSV loaded. Number of rows:", len(rows))
print("Emails from CSV:")
for r in rows:
    print("-", r["email"])

# --- EXCEPTION HANDLING PRACTICE ---
try:
    with open("missing_file.json", "r") as f:
        data = f.read()
        print("File contents:", data)
except FileNotFoundError:
    print("⚠️ File not found. Please check the filename.")
except PermissionError:
    print("⚠️ You don’t have permission to open this file.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
else:
    print("✅ File read successfully!")
finally:
    print("Done attempting to open file.\n")

import requests
def fetch_users_from_api():
    """Fetch example user data from a free API and print the first few entries."""
    print("🌍 Fetching user data from API...")
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
        response.raise_for_status()  # raises HTTPError if bad response (4xx, 5xx)
        data = response.json()
        print(f"✅ Retrieved {len(data)} users.")
        for user in data[:3]:  # just show 3 for brevity
            print(f"- {user['name']} ({user['email']})")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Network or API error: {e}")

# call the function
fetch_users_from_api()


# you’ve now practiced all the core pieces from tonight’s outline:

# file handles (open, modes)

# JSON read/write (json.dump, json.load)

# CSV read/write (csv.DictWriter, csv.DictReader)

# exception handling (try/except/else/finally)

# API request (requests.get, .json(), .raise_for_status())


# --- FULL FLOW: API -> JSON file -> CSV file ---
import json, csv, requests

def fetch_save_transform():
    print("🌍 Fetching API users and saving to files...")
    try:
        resp = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
        resp.raise_for_status()
        data = resp.json()  # list of user dicts

        # 1) Save the raw API data as JSON (pretty-printed)
        with open("api_users.json", "w") as f:
            json.dump(data, f, indent=2)
        print("✅ Saved api_users.json")

        # 2) Transform + save as CSV (choose a few useful columns)
        fieldnames = ["id", "name", "username", "email", "city"]
        with open("api_users.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for u in data:
                writer.writerow({
                    "id": u.get("id"),
                    "name": u.get("name"),
                    "username": u.get("username"),
                    "email": u.get("email"),
                    "city": (u.get("address") or {}).get("city"),
                })
        print("✅ Saved api_users.csv")

        # (Optional) quick preview
        print("Preview (first 2):")
        for u in data[:2]:
            print("-", u["name"], "/", u["email"])

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Network or API error: {e}")

# call the full flow
fetch_save_transform()
