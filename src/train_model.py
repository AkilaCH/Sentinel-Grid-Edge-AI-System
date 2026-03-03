import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import os

from audio_processor import process_audio_to_matrix, AUDIO_FILE_PATH
from anomaly_model import AcousticAutoencoder

MODEL_SAVE_PATH = "../models/sentinel_brain.pth"

def train_ai():
    print("=== Project Sentinel-Grid: Phase 3.5 (Optimized Training) ===")
    
    mfcc_matrix = process_audio_to_matrix(AUDIO_FILE_PATH)
    if mfcc_matrix is None:
        return
    
    mfcc_features = mfcc_matrix.T  

    min_val = np.min(mfcc_features)
    max_val = np.max(mfcc_features)
    
   
    scaled_features = (mfcc_features - min_val) / (max_val - min_val + 1e-10)
    

    training_data = torch.tensor(scaled_features, dtype=torch.float32)
    
    INPUT_SIZE = 13
    ai_brain = AcousticAutoencoder(input_features=INPUT_SIZE)
    
    criterion = nn.MSELoss() 
    optimizer = optim.Adam(ai_brain.parameters(), lr=0.005) 
    EPOCHS = 150 
    print(f"\n[HQ INFO] Starting Optimized Training Session... (Epochs: {EPOCHS})")
    
    for epoch in range(EPOCHS):
        optimizer.zero_grad()
        reconstructed_data = ai_brain(training_data)
        
        loss = criterion(reconstructed_data, training_data) 
        loss.backward()
        optimizer.step()
        
        if (epoch + 1) % 15 == 0:
            print(f"Epoch [{epoch+1}/{EPOCHS}] | Loss (Error Rate): {loss.item():.6f}")
            
    os.makedirs(os.path.dirname(MODEL_SAVE_PATH), exist_ok=True)
    torch.save(ai_brain.state_dict(), MODEL_SAVE_PATH)
    
    np.save("../models/scaling_factors.npy", np.array([min_val, max_val]))
    
    print(f"\n[SUCCESS] AI Brain and Scaling Factors saved securely!")
    print("=== Phase 3.5 Execution Complete! ===")

if __name__ == "__main__":
    train_ai()