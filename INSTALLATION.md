# Kinesthesis 2.0 - Installation Guide

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- A working webcam for hand and body gesture tracking
- Max/MSP 8.6 or higher (for OSC communication)

## Installation Steps

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/Kinesthesis-2.0.git
cd Kinesthesis-2.0
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Quick Start

### Running the gesture recognition system
```bash
python Kinesthesis_2_0.py
```

The application will:
- Access your webcam
- Track hand gestures and facial landmarks
- Send OSC messages to Max/MSP on `localhost:32000`
- Display real-time hand and face detection

### Stopping the application
Press the **ESC** key to quit.

## Configuration

Edit these parameters in `Kinesthesis_2_0.py`:

```python
# OSC Server settings
ip = "127.0.0.1"      # Target IP (localhost by default)
sendPort = 32000      # Target UDP port

# Detection thresholds
FINGER_UP_THRESHOLD = 0.7    # Sensitivity for finger detection
```

## OSC Message Structure

### Face Movements
- **Address**: `/face_movements`
- **Data**: `[head_y, left_eye_y, right_eye_y, mouth_y]`

### Hand Gestures
- **Address**: `/gesture`
- **Data**: `gesture_name` (e.g., "Fist", "One", "Two", etc.)

### Finger Positions
- **Address**: `/finger_0`, `/finger_1`, `/finger_2`, `/finger_3`
- **Data**: `[x, y, z]` (MIDI-mapped values 0-127)

## Supported Gestures

- **Fist**: All fingers closed
- **One**: Only index finger extended
- **Two**: Index and middle finger extended
- **Three**: Index, middle, ring finger extended
- **Four**: All fingers except thumb extended
- **Five**: All fingers extended (open hand)

## Troubleshooting

### No camera feed
- Check if your webcam is connected and accessible
- Verify camera permissions in system settings
- Try restarting the application

### OSC messages not reaching Max/MSP
- Ensure Max/MSP is running and listening on port 32000
- Check firewall settings
- Verify IP address matches (127.0.0.1 for localhost)

### Poor hand detection
- Ensure adequate lighting
- Use the `min_detection_confidence` and `min_tracking_confidence` parameters
- Current default: 0.5 (adjust for different environments)

## System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.8 | 3.11+ |
| RAM | 4GB | 8GB+ |
| Processor | Dual-core | Quad-core+ |
| Webcam | 720p | 1080p+ |

## Dependencies Overview

- **mediapipe**: Hand and facial landmark detection
- **opencv-python**: Computer vision and video capture
- **python-osc**: OSC communication protocol
- **numpy**: Numerical operations
- **scipy**: Signal processing (optional)

## Performance Tips

1. Reduce video resolution if experiencing lag
2. Adjust detection confidence thresholds
3. Ensure adequate CPU resources
4. Use a high-quality webcam for best results

## License
[Specify your license here]

## Support
For issues or questions, please open an issue on GitHub.

## Citation
If you use Kinesthesis 2.0 in your work, please cite:
```
Telemachus Moussas. Kinesthesis 2.0: Gesture-Controlled Interactive Vocal 
Augmentation System. [Year]
```
