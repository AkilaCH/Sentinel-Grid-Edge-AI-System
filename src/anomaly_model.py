import torch
import torch.nn as nn

class AcousticAutoencoder(nn.Module):
    """
    Project Sentinel-Grid: Core AI Engine
    Architecture: Deep Neural Network Autoencoder
    Purpose: Learns the 'normal' acoustic signature of a machine.
    """
    def __init__(self, input_features):
        super(AcousticAutoencoder, self).__init__()
        
        self.encoder = nn.Sequential(
            nn.Linear(input_features, 64),
            nn.ReLU(True),
            nn.Linear(64, 32),
            nn.ReLU(True),
            nn.Linear(32, 16) 
        )
        
        self.decoder = nn.Sequential(
            nn.Linear(16, 32),
            nn.ReLU(True),
            nn.Linear(32, 64),
            nn.ReLU(True),
            nn.Linear(64, input_features),
            nn.Sigmoid()  
        )

    def forward(self, x):
        """
        The forward pass: Data flows through the Encoder, then the Decoder.
        """
        compressed_state = self.encoder(x)
        reconstructed_audio = self.decoder(compressed_state)
        return reconstructed_audio


if __name__ == "__main__":
    print("=== Project Sentinel-Grid: Phase 2 (AI Architecture Test) ===")
    
    INPUT_SIZE = 13 
    
    ai_brain = AcousticAutoencoder(input_features=INPUT_SIZE)
    print("[HQ INFO] AI Model Architecture Successfully Initialized:")
    print(ai_brain)

    dummy_audio_frame = torch.rand((1, INPUT_SIZE)) 
    
    output_frame = ai_brain(dummy_audio_frame)
    
    print(f"\n[SUCCESS] Dummy Input Shape: {dummy_audio_frame.shape}")
    print(f"[SUCCESS] Reconstructed Output Shape: {output_frame.shape}")
    print("=== Phase 2 Execution Complete! Ready for Training Loop. ===")