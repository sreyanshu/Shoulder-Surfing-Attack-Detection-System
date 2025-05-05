import pyttsx3
import pyautogui
from datetime import datetime
import cv2

def trigger_alert():
    engine = pyttsx3.init()
    engine.say("Hey! Someone is watching your screen.")
    engine.say("Thanks for using Shoulder Surfing Detection")
    engine.runAndWait()

def blur_screen():
    pyautogui.hotkey('win', 'd')

def save_intrusion_frame(frame):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"screenshots/intrusion_{timestamp}.png"
    cv2.imwrite(filename, frame)

def log_intrusion(count):
    with open("logs/intrusions_log.txt", "a") as f:
        f.write(f"[{datetime.now()}] Intrusion Detected! Faces Detected: {count}\n")
