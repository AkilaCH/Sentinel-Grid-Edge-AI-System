import json
import os
from datetime import datetime

ALERTS_FILE = os.path.join(os.path.dirname(__file__), "../shared/alerts.json")

def report_to_dashboard(status, error_score, node_id="EDGE-NODE-01"):
    """
    Simulates a Cloud Dispatch by writing alert data to a shared JSON file.
    Args:
        status (str): "NORMAL" or "ANOMALY"
        error_score (float): The MSE loss from the Autoencoder
        node_id (str): ID of the monitoring station
    """
    os.makedirs(os.path.dirname(ALERTS_FILE), exist_ok=True)
    
    new_alert = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": status,
        "error_score": f"{error_score:.6f}",
        "node_id": node_id,
        "location": "Colombo Factory - Floor 01"
    }

    alert_history = []
    if os.path.exists(ALERTS_FILE):
        try:
            with open(ALERTS_FILE, "r") as f:
                alert_history = json.load(f)
                alert_history = alert_history[-19:] 
        except (json.JSONDecodeError, FileNotFoundError):
            alert_history = []

    alert_history.append(new_alert)

    try:
        with open(ALERTS_FILE, "w") as f:
            json.dump(alert_history, f, indent=4)
        
        print(f"[LOCAL CLOUD] Mission Status Synced: {status} | Score: {error_score:.6f}")
        return True
    except Exception as e:
        print(f"[CRITICAL ERROR] Failed to sync with Dashboard: {e}")
        return False

if __name__ == "__main__":
    print("=== Sentinel-Grid: Local Reporter Internal Test ===")
    test_success = report_to_dashboard("NORMAL", 0.000913)
    if test_success:
        print("[SUCCESS] Test data successfully written to shared/alerts.json")