from ultralytics import YOLO

# Load the pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

# Export to ONNX format with fixed input size
model.export(format="onnx", imgsz=640, opset=12)