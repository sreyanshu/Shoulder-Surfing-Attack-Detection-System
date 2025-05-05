import cv2

def initialize_camera():
    cap = cv2.VideoCapture(0)
    return cap
