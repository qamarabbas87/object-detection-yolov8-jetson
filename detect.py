import cv2

# Load your ONNX model
model_path = "model/yolov8.onnx"
net = cv2.dnn.readNetFromONNX(model_path)

# Load video (0 for webcam, or replace with video file path)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Prepare the frame for the model
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (640, 640), swapRB=True, crop=False)
    net.setInput(blob)

    # Run inference
    outputs = net.forward()

    # (Optional) Post-process outputs depending on your model structure
    # Here you'd parse outputs and draw boxes (this step varies by model)

    cv2.imshow("YOLOv8 Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
