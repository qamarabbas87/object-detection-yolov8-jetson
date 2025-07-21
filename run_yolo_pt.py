from ultralytics import YOLO

# Load pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

# Run real-time detection using your webcam
model.predict(source=0, show=True)


# Safely close OpenCV windows
cv2.destroyAllWindows()
