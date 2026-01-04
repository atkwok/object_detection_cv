from ultralytics import YOLOWorld

# Initialize a YOLO-World model
model = YOLOWorld("yolo11m.pt")  # or select yolov8m/l-world.pt for different sizes

CLASSES = [0, 1, 2, 3, 4, 5, 6, 8, 14, 15, 16, 17, 19, 39, 54, 56, 57, 58, 60, 62]
# model.set_classes(["airplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "dining table", "dog", "horse", "motorbike", "person", "potted plant", "donut", "sofa", "train", "tv monitor", ""])

# Execute inference with the YOLOv8s-world model on the specified image
results = model.predict("synthetic_all/", augment=True, save_txt=True, classes=CLASSES)

# Show results
# results[0].show()

# for result in results:
#     # Normalized xywh format (numpy array)
#     boxes_normalized = result.boxes.xywhn.cpu().numpy()

#     # Absolute pixel xyxy format (numpy array)
#     boxes_pixels = result.boxes.xyxy.cpu().numpy()

#     # Convert to a pandas DataFrame
#     df = result.pandas().xyxy[0]


#Notes
# Predict 6 - all with sheep
# Predict 7 - donut addendum
# Predict 8 - yolo11m ALL synthetic (USE THIS)