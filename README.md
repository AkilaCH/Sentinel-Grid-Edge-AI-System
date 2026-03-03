**Project Sentinel-Grid**
Industrial-Grade Acoustic Anomaly Detection System

Project Sentinel-Grid is an end-to-end AI monitoring solution designed to identify machinery failures before they become catastrophic. 
By analyzing industrial acoustic signatures at the Edge, the system identifies deviations from a healthy operational baseline, providing 
real-time alerts through a high-performance dashboard.

**System Architecture**
The system operates as a high-speed telemetry pipeline, processing raw audio into actionable industrial intelligence.

1. Sensor Node (Ears): Captures raw acoustic data from industrial machinery using high-fidelity microphones.

2. Signal Processing (Extraction): Converts raw audio waves into a 13-feature MFCC (Mel-frequency cepstral coefficients) matrix to represent the sound’s mathematical "DNA".

3. The AI Brain (Inference): A PyTorch-based Deep Autoencoder analyzes the compressed features to calculate a reconstruction error.

4. Command Center (Output): A Next.js dashboard visualizes the machine's health and triggers sub-second alerts when an anomaly is detected.

**Deep Learning Architecture: The Autoencoder**
Unlike standard classification models, Sentinel-Grid uses an Unsupervised Autoencoder. This is critical for industrial settings because it is impossible to train a model on every possible way a machine might fail.

- The Encoder: Compresses 13 input features into a 16-unit "Bottleneck" or Latent Space. It forces the AI to learn only the most critical patterns of a healthy machine sound.
- The Decoder: Attempts to rebuild the original signal from the compressed bottleneck.
- The Anomaly Logic: If a machine starts making an unusual sound (e.g., a loose bolt or bearing failure), the AI’s bottleneck won't recognize the pattern. This causes a spike in the Mean Squared Error (MSE).

**Mathematical Verification**
The system calculates the Reconstruction Loss ($MSE$) to determine the verdict:

<img width="1908" height="522" alt="e6eb725a-e263-4dd0-aa80-7312d699a275" src="https://github.com/user-attachments/assets/53aabfec-f330-4933-8567-59f56e76fd8b" />

If $MSE > Threshold$ (0.02), a RED ALERT is dispatched.

-----------------------------------------------------------------------------------------

**Tech Stack & Engineering Depth**
Backend & AI (Python Engine)
- PyTorch: Used for building and training the Deep Neural Network.
- Librosa: Handles high-performance signal processing and MFCC extraction.
- NumPy: Manages high-speed matrix transformations and Min-Max scaling for data normalization.

**Frontend (Command Center)**
- Next.js 14 & React: Built with the App Router for optimal performance.
- Tailwind CSS: Aerospace-inspired tactical UI for real-time monitoring.
- Polling Logic: Synchronizes with the Edge node every 3 seconds to reflect live sensor data.

-----------------------------------------------------------------------------------------

**Intelligence Reports (Live Demos)**
- Phase 1: Baseline Maintenance
When the machine operates within healthy parameters, the AI successfully reconstructs the signal with minimal error (~0.0009).

<img width="1866" height="657" alt="ef03e720-deb2-4bc5-92b2-1839864d1f89" src="https://github.com/user-attachments/assets/cfba00b2-93cd-4e97-8d3e-8e9e2cb26a50" />

- Phase 2: Anomaly Detection
When an external acoustic intruder or machine fault is introduced, the MSE score jumps by over 40x (e.g., 0.041), triggering the autonomous alert system.

-----------------------------------------------------------------------------------------

**Project Structure & Git Strategy**
The repository is structured following professional DevOps practices. Note that large binaries and local environment data are excluded via .gitignore to maintain a lean production-ready codebase.

sentinel-grid-edge/
├── dashboard/          # Next.js Command Center
├── src/                # Python AI & Processing Logic
├── models/             # Trained AI Weights (.pth) [Git Ignored]
├── data/               # Raw Acoustic Datasets [Git Ignored]
└── shared/             # Real-time Data Bridge (Mock-Cloud)

**Installation & Setup**
1. Configure the Python Edge Node
cd src
python -m venv .venv
source .venv/bin/activate  # Windows: .\.venv\Scripts\activate
pip install -r requirements.txt

2. Train the AI Brain
python train_model.py

3. Launch the Dashboard
cd dashboard
npm install
npm run dev

4. Execute Real-time Detection
cd src
python detect_anomaly.py
