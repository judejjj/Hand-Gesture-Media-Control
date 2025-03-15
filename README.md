# 🎮 Hand Gesture Controlled Media Player

## 📌 Overview
This project allows you to control media playback using **hand gestures** detected via **OpenCV** and **Mediapipe**. No physical buttons or remotes needed—just your hand!

## 🎥 How It Works
- Uses **OpenCV** to capture video.
- Uses **Mediapipe** to track your hand.
- Detects **only one hand** and ignores the other.
- Sends keyboard shortcuts based on the number of fingers detected.

## 🎯 Controls

| Fingers Up | Action        |
| ---------- | ------------- |
| 0 Fingers  | Mute          |
| 1 Finger   | Seek Forward  |
| 2 Fingers  | Seek Backward |
| 3 Fingers  | Volume Up     |
| 4 Fingers  | Volume Down   |
| 5 Fingers  | Play/Pause    |

## 🔧 Prerequisites
Before running this project, ensure you have:

✅ **Python (3.7 or later) installed.** [Download Python](https://www.python.org/downloads/)  
✅ A **camera (webcam)** connected to your system.

## 🚀 Getting Started
Since the **virtual environment (`media`) is already included**, you **don’t** need to install dependencies manually. Just activate it and run the script.

### 1️⃣ Activate the Virtual Environment

#### On Windows:
```bash
media\Scripts\activate
```

#### On macOS/Linux:
```bash
source media/bin/activate
```

### 2️⃣ Install Dependencies
If you need to install all required dependencies manually, run:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Script
```bash
python Gesture.py
```

## 📝 Notes
✅ Works best with a well-lit background.  
✅ Keep your hand in front of the camera for best tracking.  
✅ Ensure no second hand is detected to avoid errors.  

## 💡 Future Improvements
🚀 Add more custom gestures for advanced control.  
🚀 Improve accuracy when hands are rotated.  
🚀 Support for more media applications like Netflix, Spotify, and YouTube.  

## 🏆 Credits
Built using Python, OpenCV, and Mediapipe.
