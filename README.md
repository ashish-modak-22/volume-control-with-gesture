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
## 1. Webcam Input

The webcam continuously captures live video frames.

Each frame is processed individually to detect hand movement.

OpenCV handles:
- Camera access
- Frame reading
- Image conversion
- Displaying output


## 2. Hand Landmark Detection

- MediaPipe provides a pre-trained hand tracking model.

- It detects 21 different points on the hand.

Example landmarks:
- Wrist
- Thumb joints
- Index finger joints
- Middle finger joints
- Ring finger joints
- Pinky joints

Each landmark contains:
- X coordinate
- Y coordinate
- Z coordinate

These coordinates represent the position of different hand points.


## 3. Gesture Recognition Logic

The project uses the distance between:

- Thumb Tip + Index Finger Tip to recognize the gesture.

- The distance is calculated using Euclidean distance:

- distance = √((x2-x1)² + (y2-y1)²)

When the fingers move:
- Distance increases → Volume increases
- Distance decreases → Volume decreases


## 4. Volume Mapping

Raw finger distance values are converted into a volume range.

Example:
```
Finger Distance

20 pixels

      ↓

0% Volume


150 pixels

      ↓

100% Volume
```
This creates a smooth control system.

---

# 📂 Project Structure
```
Volume-Control-With-Gesture
   │
   ├── main.py
   │
   ├── HandTrackingModule.py
   │
   ├── requirements.txt
   │
   └── README.md
```
---

# 📄 File Explanation
## main.py

Contains:
- Main application logic
- Webcam initialization
- Gesture processing
- Volume control


## HandTrackingModule.py

Contains:
- HandDetector class
- MediaPipe initialization
- Hand landmark detection functions

This makes the project modular and reusable.

---
