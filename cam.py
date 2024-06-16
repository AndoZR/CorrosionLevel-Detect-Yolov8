from ultralytics import YOLO

# Load the model
model = YOLO("D:/Ando File 4 Kuliah/BELAJAR SKRIPSI/COMPUTER VISION/CAPSTONE HACTIVE/yolov8-streamlit-detection-tracking/weights/bestyolo8.pt")

# Perform object detection
results = model("0", show=True, conf=0.5)
