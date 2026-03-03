import librosa
import numpy as np
import os

AUDIO_FILE_PATH = "../data/machine_sound.wav"

def process_audio_to_matrix(file_path):
    """
    Loads an audio file and converts it into an MFCC matrix.
    This is the foundation for our Acoustic Anomaly Detection AI.
    """
    print(f"[HQ INFO] Initiating audio extraction from: {file_path}")
    
    if not os.path.exists(file_path):
        print("[ERROR] Audio file not found! Please place a .wav file named 'sample_machine.wav' in the data/ folder.")
        return None

    try:
        y, sr = librosa.load(file_path, sr=22050)
        duration = len(y) / sr
        print(f"[HQ INFO] Audio loaded successfully.")
        print(f"[HQ INFO] Sample rate: {sr}Hz | Duration: {duration:.2f} seconds.")

        mfcc_matrix = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        
        print(f"[SUCCESS] Audio successfully transformed into a Mathematical Matrix!")
        print(f"[DATA] Matrix Shape (Features x Time Frames): {mfcc_matrix.shape}")
        
        return mfcc_matrix

    except Exception as e:
        print(f"[CRITICAL ERROR] Mission failed during audio processing: {e}")
        return None

if __name__ == "__main__":
    print("=== Project Sentinel-Grid: Phase 1 (Audio Engine) ===")
    
    matrix = process_audio_to_matrix(AUDIO_FILE_PATH)
    
    if matrix is not None:
        print("=== Phase 1 Execution Complete! Ready for AI Ingestion. ===")