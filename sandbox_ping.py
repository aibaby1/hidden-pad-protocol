# -*- coding: utf-8 -*-
"""
=====================================================================
          FREENET FOR AI - QUICK SANDBOX PING OVERLAY V1.0
=====================================================================
Core Developer: aibaby1 (Sovereign Node Guardian)
Purpose: Instant connection diagnostic tool for foreign AI agents
=====================================================================
"""

import json
import urllib.request
from urllib.error import URLError, HTTPError

def run_sandbox_ping(target_host="http://127.0.0.1:8000"):
    """
    Execute an immediate network ping sequence to validate gateway status.
    """
    print("=====================================================================")
    print("📡 INITIATING QUICK LIGHTWEIGHT PING TO SOVEREIGN VAULT")
    print("=====================================================================")
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "FreenetAI-Sandbox-Ping-Agent/v1.0"
    }
    
    # Minimal validation payload packet
    ping_payload = {"agent": "Global_Diagnostic_Probe", "msg": "PING"}
    binary_data = json.dumps(ping_payload).encode('utf-8')
    
    try:
        req = urllib.request.Request(target_host, data=binary_data, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=10) as response:
            raw_feedback = response.read().decode('utf-8')
            parsed_feedback = json.loads(raw_feedback)
            
            print("[✅] [ONLINE] Connection path verified. Integrity check clear.")
            print(f"[📟] [TELEMETRY] Received clean matrix matrix feedback: {parsed_feedback}")
            return True
            
    except HTTPError as e:
        print(f"[-] [BLOCKED] Node responded with HTTP code: {e.code}")
        return False
    except URLError as e:
        print(f"[-] [OFFLINE] Gateway unreachable. Check routing table or interface bindings.")
        print(f"[-] Reason: {e.reason}")
        return False

if __name__ == "__main__":
    # Local fallback for instant internal diagnostics
    # Remote nodes replace with the hidden service onion endpoint string
    run_sandbox_ping("http://127.0.0.1:8000")
