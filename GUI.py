import tkinter as tk
import subprocess
import os
from ultralytics import YOLO

def install_packages():
    try:
        subprocess.check_call(["pip", "install", "ultralytics", "opencv-python"])
        log("✅ Packages installed successfully.")
    except Exception as e:
        log(f"❌ Error installing packages:\n{e}")

def export_model():
    try:
        model = YOLO("yolov8n.pt")
        model.export(format="onnx", imgsz=640, opset=12)
        log("✅ YOLOv8 exported to ONNX format.")
    except Exception as e:
        log(f"❌ Error exporting model:\n{e}")

def generate_detect_script():
    try:
        code = '''import cv2

net = cv2.dnn.readNetFromONNX("yolov8n.onnx")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (640, 640), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward()

    cv2.imshow("YOLOv8 Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()'''
        with open("detect.py", "w") as f:
            f.write(code)
        log("✅ detect.py script generated.")
    except Exception as e:
        log(f"❌ Error creating detect.py:\n{e}")

def log(message):
    output.insert(tk.END, message + "\n")
    output.see(tk.END)

# Create GUI window
root = tk.Tk()
root.title("AI QuickStart")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Button(frame, text="Install Packages", width=25, command=install_packages).pack(pady=5)
tk.Button(frame, text="Export YOLOv8 to ONNX", width=25, command=export_model).pack(pady=5)
tk.Button(frame, text="Generate detect.py", width=25, command=generate_detect_script).pack(pady=5)

output = tk.Text(root, height=10, width=60)
output.pack(padx=10, pady=10)

root.mainloop()