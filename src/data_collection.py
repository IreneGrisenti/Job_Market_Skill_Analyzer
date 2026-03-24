import requests
import json
import time
import os

# Base address of Arbetsförmedlingen
url = "https://jobsearch.api.jobtechdev.se/search"

search_terms = [
    "data scientist",
    "data analyst",
    "data engineer",
    "machine learing",
    "business intelligence",
    "business analyst",
    "AI engineer",
    "MLOps",
    "datavetenskap",
    "dataanalytiker",
    "dataingenjör",
    "maskininlärning",
    "BI-utvecklare",
    "affärsanalytiker",
    "AI ingenjör"
]

all_jobs = [] # List to collect the jobs
seen_ids = set() # avoids duplicates

for term in search_terms:
    offset = 0 # tracks how far into the results I am
    total = None # will store how many results the API says exist for this term

    while total is None or offset < total: # keeps looking until all pages have been fetched
        params = { # the parameters to add to the url
            "q": term,
            "limit": 100, # the max n of requests
            "offset": offset # skips n results as if they were pages
        }
        response = requests.get(url, params=params) # this sends the request
        data = response.json() # the response is in json so it parses it into a dict

        if total is None:
            total = data["total"]["value"] # tells you the total result

        jobs = data.get("hits", [])
        if not jobs:
            break

        new_jobs = 0
        for job in jobs:
            if job["id"] not in seen_ids:
                seen_ids.add(job["id"])
                all_jobs.append(job)
                new_jobs += 1

        offset += 100
        time.sleep(0.5)

    print(f"'{term}': {total} found, {len(all_jobs)} total unique so far")

print(f"\nTotal unique jobs collected: {len(all_jobs)}")

os.makedirs("../data", exist_ok=True)

try:
    with open("/home/irene/Desktop/Job Market Skill Analyzer/data/raw_jobs.json", "w", encoding="utf-8") as f:
        json.dump(all_jobs, f, ensure_ascii=False, indent=2)
    print("✅ File saved successfully!")
except Exception as e:
    print(f"❌ Save failed: {e}")