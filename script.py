import requests
import time
import random
import os
from datetime import datetime

# URLs from GitHub Secrets
URL_A = os.environ.get("URL_A")
URL_B = os.environ.get("URL_B")

# Standard header to look like a real browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def run():
    # --- 1. RANDOM START (0 to 2.5 Hours) ---
    pre_wait = random.randint(0, 9000)
    # flush=True ensures this message shows up in GitHub Actions immediately
    print(f"[{datetime.now()}] GitHub Triggered. Waiting {pre_wait//60}m {pre_wait%60}s before starting.", flush=True)
    time.sleep(pre_wait)

    # --- 2. REQUEST A (90s Timeout) ---
    print(f"[{datetime.now()}] Sending Request A...", flush=True)
    try:
        response_a = requests.get(URL_A, headers=HEADERS, timeout=90)
        print(f"Request A Status Code: {response_a.status_code}", flush=True)
    except requests.exceptions.Timeout:
        print("Error: Request A timed out after 1:30 minutes.", flush=True)
    except Exception as e:
        print(f"Error on A: {e}", flush=True)

    # --- 3. RANDOM GAP (2 to 4 Minutes) ---
    gap = random.randint(120, 240)
    print(f"Waiting {gap}s before Request B...", flush=True)
    time.sleep(gap)

    # --- 4. REQUEST B (90s Timeout) ---
    print(f"[{datetime.now()}] Sending Request B...", flush=True)
    try:
        response_b = requests.get(URL_B, headers=HEADERS, timeout=90)
        print(f"Request B Status Code: {response_b.status_code}", flush=True)
    except requests.exceptions.Timeout:
        print("Error: Request B timed out after 1:30 minutes.", flush=True)
    except Exception as e:
        print(f"Error on B: {e}", flush=True)

if __name__ == "__main__":
    run()
