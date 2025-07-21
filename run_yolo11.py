from ultralytics import YOLO

# Load YOLOv11n model (Nano version for speed)
model = YOLO("yolo11n.pt")

# Run detection on webcam
model.predict(source=0, show=True)


# Safely close OpenCV windows
cv2.destroyAllWindows()