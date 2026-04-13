import cv2
import torch
import time
from ultralytics import YOLO
from playsound import playsound  # To play siren sound
import threading  # For playing siren without blocking detection

# Load the trained YOLO model
model = YOLO("D:\\stl\\best.pt")  # Change path if needed

# Initialize webcam
cap = cv2.VideoCapture(0)

siren_active = False  # Flag to check if siren is currently playing
detection_start_time = 0  # Time when monkey detection starts
DETECTION_THRESHOLD = 2  # Detection should be continuous for 2 seconds to trigger the siren

def play_siren():
    global siren_active
    siren_active = True
    playsound("D:\\stl\\alert1.mp3")  # Replace with actual siren sound file
    siren_active = False  # Reset after sound completes

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO model on the frame
    results = model(frame)

    monkey_detected = False  # Flag to check if monkey is detected in the frame

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])  # Get detected class ID
            confidence = box.conf[0]  # Confidence score

            if class_id == 0 and confidence > 0.5:  # Change ID if needed
                monkey_detected = True

                # Draw bounding box
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, "Monkey Detected!", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

                # If it's the first time the monkey is detected, start tracking
                if detection_start_time == 0:
                    detection_start_time = time.time()

    # If the monkey is detected for a continuous 2 seconds
    if monkey_detected:
        if time.time() - detection_start_time >= DETECTION_THRESHOLD and not siren_active:
            threading.Thread(target=play_siren).start()
            detection_start_time = 0  # Reset the timer after triggering siren

    # If the monkey is no longer detected, reset the detection timer
    if not monkey_detected:
        detection_start_time = 0

    # Show frame
    cv2.imshow("Monkey Detection", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
