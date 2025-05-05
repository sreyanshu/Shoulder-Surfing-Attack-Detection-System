import cv2
import mediapipe as mp

def is_user_looking_away(results):
    # Basic heuristic based on nose & eyes position
    if not results.multi_face_landmarks:
        return False

    face = results.multi_face_landmarks[0]
    # Use landmarks to estimate face direction
    nose_tip = face.landmark[1].x
    if nose_tip < 0.4 or nose_tip > 0.6:
        return True
    return False