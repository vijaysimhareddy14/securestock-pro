# threat_engine.py

import random

def simulate_threat():
    event = random.choice(["none", "api_delay", "suspicious_spike", "ddos"])
    if event == "none":
        return {"status": "low", "message": "System operating normally."}
    elif event == "api_delay":
        return {"status": "medium", "message": "API latency increased."}
    elif event == "suspicious_spike":
        return {"status": "medium", "message": "Abnormal volume spike detected."}
    else:
        return {"status": "high", "message": "DDoS pattern detected. Security Risk!"}
