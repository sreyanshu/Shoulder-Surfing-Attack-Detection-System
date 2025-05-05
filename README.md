# Shoulder Surfing Attack Detection System(AI-POWERED) 👁️‍🗨️

# Overview
This project detects potential **shoulder surfing attacks** using a webcam and real-time computer vision. It warns the user when someone appears behind or beside them, peeking at their screen.

#  Features
- Detects multiple faces using OpenCV.
- Triggers a voice alert if more than one face is detected.
- Minimizes all windows to protect on-screen data.
- Logs incidents with timestamps and saves evidence screenshots.

# Technologies
- Python
- OpenCV
- Mediapipe
- pyttsx3 (Text-to-Speech)
- pyautogui (Screen Control)



# How to Run
1. Install dependencies:

pip install opencv-python mediapipe pyttsx3 pyautogui


2. Run the main script:

python main.py


3. Sit in front of the webcam and simulate a shoulder surfing attempt!

# Sample Output
- Voice alert:
### "hey! Someone is watching your screen."###

- Screenshot saved in `screenshots/`.
- Log entry saved in `logs/intrusions_log.txt`.


