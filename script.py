import requests
import time
import random
import os
from datetime import datetime

# Grab variables from the 'env' section of the YAML
URL_A = os.environ.get("URL_A")
TOKEN = os.environ.get("MY_API_TOKEN")

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28',
    'User-Agent': 'Python-Requests'
}

DATA = '{"ref": "main"}'

def run():
    # --- SAFE DEBUG CHECK ---
    print(f"[{datetime.now()}] Checking Environment...", flush=True)
    if not URL_A:
        print("❌ ERROR: URL_A is missing from Secrets!", flush=True)
    if not TOKEN:
        print("❌ ERROR: TOKEN is missing from Secrets!", flush=True)
    else:
        # This tells us it exists without revealing the secret
        print(f"✅ Token received (Length: {len(TOKEN)})", flush=True)

    # --- 1. RANDOM START ---
    pre_wait = random.randint(0, 0)
    print(f"Waiting {pre_wait//60}m before API calls...", flush=True)
    time.sleep(pre_wait)

    # --- 2. FIRST CALL ---
    print(f"Sending First API Dispatch to {URL_A}...", flush=True)
    try:
        resp1 = requests.post(URL_A, headers=HEADERS, data=DATA, timeout=90)
        print(f"First Request Status: {resp1.status_code}", flush=True)
        if resp1.status_code == 401:
            print("Status 401: GitHub is still rejecting the token. Check 'workflow' permissions.", flush=True)
    except Exception as e:
        print(f"Error: {e}", flush=True)

    # --- 3. GAP ---
    time.sleep(random.randint(0, 0))

    # --- 4. SECOND CALL ---
    try:
        resp2 = requests.post(URL_A, headers=HEADERS, data=DATA, timeout=90)
        print(f"Second Request Status: {resp2.status_code}", flush=True)
    except Exception as e:
        print(f"Error: {e}", flush=True)

if __name__ == "__main__":
    run()
