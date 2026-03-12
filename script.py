import requests
import time
import random
import os
from datetime import datetime

# URLs and Token from environment
URL_A = os.environ.get("URL_A")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

# GitHub API Headers
HEADERS = {
    'Authorization': f'Bearer {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28',
    'User-Agent': 'Python-Requests'
}

# The body required by GitHub to know which branch to run
DATA = '{"ref": "main"}'

def run():
    # --- 1. RANDOM START (0 to 2.5 Hours) ---
    pre_wait = random.randint(0, 9000)
    print(f"[{datetime.now()}] Triggered. Waiting {pre_wait//60}m before starting.", flush=True)
    time.sleep(pre_wait)

    # --- 2. FIRST EXECUTION ---
    print(f"[{datetime.now()}] Sending First API Dispatch...", flush=True)
    try:
        # GitHub Dispatch requires a POST request
        resp1 = requests.post(URL_A, headers=HEADERS, data=DATA, timeout=90)
        # 204 is the standard "Success" code for this GitHub API
        print(f"First Request Status: {resp1.status_code}", flush=True)
    except Exception as e:
        print(f"Error on First Request: {e}", flush=True)

    # --- 3. RANDOM GAP (2 to 4 Minutes) ---
    gap = random.randint(120, 240)
    print(f"Waiting {gap}s before repeating...", flush=True)
    time.sleep(gap)

    # --- 4. SECOND EXECUTION ---
    print(f"[{datetime.now()}] Sending Second API Dispatch...", flush=True)
    try:
        resp2 = requests.post(URL_A, headers=HEADERS, data=DATA, timeout=90)
        print(f"Second Request Status: {resp2.status_code}", flush=True)
    except Exception as e:
        print(f"Error on Second Request: {e}", flush=True)

if __name__ == "__main__":
    run()
