from ultralytics import YOLO
import cv2
import time
import simpleaudio as sa  # For sound alerts

# Load YOLO model (Pre-trained or Custom)
#model = YOLO("runs/detect/exp12/weights/best.pt", task="detect")
model = YOLO("yolov5s.pt")  # Change to "yolov5s.pt" if using the pre-trained model
  # Change to "yolov5s.pt" if using the pre-trained model

# Set the target class (change this to your custom class name)
TARGET_CLASS = "person"  # Change based on your trained model
alert_duration = 5  # Trigger alert if detected for more than 5 sec

# Load sound alert
wave_obj = sa.WaveObject.from_wave_file("alert.wav")  # Make sure you have this file

# Start video capture
cap = cv2.VideoCapture(0)  # Use "video.mp4" for a video file

start_time = None
class_detected = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv5 inference
    results = model(frame)

    detected = False  # Reset detection flag

    # Process results
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            confidence = float(box.conf[0])
            class_name = model.names[cls_id]

            # Check if detected class is the target class
            if class_name == TARGET_CLASS and confidence > 0.5:
                detected = True
                break

    # Timer logic
    if detected:
        if not class_detected:
            start_time = time.time()  # Start timer when first detected
            class_detected = True
        else:
            elapsed_time = time.time() - start_time
            if elapsed_time >= alert_duration:
                print("Alert! Target class detected for over 5 seconds.")
                wave_obj.play()
                class_detected = False  # Reset to prevent repeated alerts
    else:
        class_detected = False  # Reset if target class disappears

    # Display the output frame
    cv2.imshow("YOLOv5 Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
