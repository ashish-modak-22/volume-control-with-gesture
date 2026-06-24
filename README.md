# 🎚️Volume Control Using Hand Gesture 

A computer vision based volume control system that allows users to control system volume using real-time hand gestures without touching any physical buttons or devices.
The project uses OpenCV for image processing and MediaPipe for real-time hand tracking. The system detects hand landmarks, calculates finger distance, and maps the gesture movement into Windows system volume changes.
This project demonstrates the implementation of Human Computer Interaction (HCI) using computer vision.

---

# 📌 About The Project

Traditional computer interaction requires physical input devices like keyboards, mice, or buttons to control system functions.

This project creates a touchless interaction system where a user's hand becomes the controller.

### Using a webcam:

- The hand is detected in real time
- Important hand points are extracted
- Finger movement is analyzed
- Gesture distance is converted into volume level
- System volume changes dynamically

---

### The main objective of this project is to explore:

- Computer Vision
- Hand Tracking
- Gesture Recognition
- Real-Time Image Processing
- Human Computer Interaction

---
# ✨ Features
- Real-time hand detection using webcam
- Tracks complete hand landmarks
- Gesture based volume adjustment
- Smooth volume control
- Modular Python architecture
- Fast and lightweight execution
- No external hardware required

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Primary Programming Language |
| **OpenCv** | Capturing webcam frames, Processing images, Drawing landmarks, Handling real-time video stream |
| **MediaPipe** | Detecting hands, Extracting hand landmarks, Tracking finger positions |
| **NumPy** | Data processing: Converts distance between landmarks to its equivalent volume |
| **Pycaw** | Accessing Windows audio API, Changing system volume programmatically |
| **Comtypes** | Used as a dependency for Pycaw communication |

---

# 🧠 Working Principle

### The complete workflow:
```
┌──────────────┐
│    Webcam    │
└──────┬───────┘
       ↓
┌────────────────────────┐
│ Capture Video Frames   │
└──────┬─────────────────┘
       ↓
┌────────────────────────┐
│ OpenCV Processing      │
└──────┬─────────────────┘
       ↓
┌────────────────────────┐
│ MediaPipe Hand Detect  │
└──────┬─────────────────┘
       ↓
┌────────────────────────┐
│ Extract Landmarks      │
└──────┬─────────────────┘
       ↓
┌────────────────────────┐
│ Calculate Finger Gap   │
└──────┬─────────────────┘
       ↓
┌────────────────────────┐
│ Convert To Volume      │
└──────┬─────────────────┘
       ↓
┌────────────────────────┐
│ System Volume Control  │
└────────────────────────┘
```
---

# 🔍 Detailed Explanation
### 1. Webcam Input

The webcam continuously captures live video frames.

Each frame is processed individually to detect hand movement.

OpenCV handles:
- Camera access
- Frame reading
- Image conversion
- Displaying output

