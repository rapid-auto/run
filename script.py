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
    # 9000 seconds = 150 minutes
    pre_wait = random.randint(0, 9000)
    print(f"[{datetime.now()}] GitHub Triggered. Waiting {pre_wait//60}m {pre_wait%60}s before starting.")
    time.sleep(pre_wait)

    # --- 2. REQUEST A (90s Timeout) ---
    print(f"[{datetime.now()}] Sending Request A...")
    try:
        response_a = requests.get(URL_A, headers=HEADERS, timeout=90)
        # ONLY PRINTING STATUS CODE
        print(f"Request A Status Code: {response_a.status_code}")
    except requests.exceptions.Timeout:
        print("Error: Request A timed out after 1:30 minutes.")
    except Exception as e:
        print(f"Error on A: {e}")

    # --- 3. RANDOM GAP (2 to 4 Minutes) ---
    gap = random.randint(120, 240)
    print(f"Waiting {gap}s before Request B...")
    time.sleep(gap)

    # --- 4. REQUEST B (90s Timeout) ---
    print(f"[{datetime.now()}] Sending Request B...")
    try:
        response_b = requests.get(URL_B, headers=HEADERS, timeout=90)
        # ONLY PRINTING STATUS CODE
        print(f"Request B Status Code: {response_b.status_code}")
    except requests.exceptions.Timeout:
        print("Error: Request B timed out after 1:30 minutes.")
    except Exception as e:
        print(f"Error on B: {e}")

if __name__ == "__main__":
    run()
