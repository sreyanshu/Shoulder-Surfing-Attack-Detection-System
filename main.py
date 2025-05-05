

import cv2
import mediapipe as mp
from face_detect import detect_faces
from alert import trigger_alert, blur_screen, log_intrusion, save_intrusion_frame
from utils import initialize_camera

cap = initialize_camera()
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

print("Shoulder Surfing Detection System Started.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = detect_faces(frame)

    if len(faces) > 1:
        trigger_alert()
        blur_screen()
        log_intrusion(len(faces))
        save_intrusion_frame(frame)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow("Shoulder Surfing Detector", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
print("Thanks for using shoulder Surfing detection")