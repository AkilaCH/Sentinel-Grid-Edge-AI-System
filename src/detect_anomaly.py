import torch
import torch.nn as nn
import numpy as np
import os

from audio_processor import process_audio_to_matrix
from anomaly_model import AcousticAutoencoder
from local_reporter import report_to_dashboard

MODEL_PATH = "../models/sentinel_brain.pth"
SCALING_PATH = "../models/scaling_factors.npy"

ANOMALY_THRESHOLD = 0.02 

def detect_anomaly(test_audio_path):
    """
    Analyzes an audio file, calculates error score using the AI Brain,
    and reports the result to the local dashboard.
    """
    print(f"=== Project Sentinel-Grid: Phase 4 (Detection Engine) ===")
    print(f"[MISSION] Scanning Target: {test_audio_path}")
    
    if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALING_PATH):
        print("[CRITICAL ERROR] AI Brain or Scaling factors missing! Run train_model.py first.")
        return

    mfcc_matrix = process_audio_to_matrix(test_audio_path)
    if mfcc_matrix is None:
        return
    mfcc_features = mfcc_matrix.T 
    
    scaling_factors = np.load(SCALING_PATH)
    min_val, max_val = scaling_factors[0], scaling_factors[1]
    
    scaled_features = (mfcc_features - min_val) / (max_val - min_val + 1e-10)
    test_tensor = torch.tensor(scaled_features, dtype=torch.float32)
    
    INPUT_SIZE = 13
    ai_brain = AcousticAutoencoder(input_features=INPUT_SIZE)
    ai_brain.load_state_dict(torch.load(MODEL_PATH))
    ai_brain.eval() 
    print("[HQ INFO] AI Brain loaded and operational.")

    criterion = nn.MSELoss()
    with torch.no_grad():
        reconstructed_data = ai_brain(test_tensor)
        error_score = criterion(reconstructed_data, test_tensor).item()
        
    print("\n" + "-"*40)
    print(f"ANALYZED ERROR SCORE : {error_score:.6f}")
    print(f"SECURITY THRESHOLD   : {ANOMALY_THRESHOLD:.6f}")
    print("-"*40)
    
    if error_score > ANOMALY_THRESHOLD:
        print("🚨 [RED ALERT] ANOMALY DETECTED! 🚨")
        status = "ANOMALY"
    else:
        print("✅ [STATUS NORMAL] Operational baseline maintained.")
        status = "NORMAL"

    report_to_dashboard(status, error_score)
    print(f"[SUCCESS] Mission Report synced to shared/alerts.json\n")

if __name__ == "__main__":
    TARGET_AUDIO = "../data/glass_break.wav" 
    detect_anomaly(TARGET_AUDIO)