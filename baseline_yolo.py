from ultralytics import YOLO

# Load a model
# model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)

# Train the model
# results = model.train(data="VOC.yaml", batch=-1, epochs=10, imgsz=416, save_period=2, device="mps", val=False)

# # Load a model
# model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)

# # Train the model
# results = model.train(data="VOC_replaced_baseline.yaml", batch=-1, epochs=10, imgsz=416, save_period=2, device="mps", val=False)




# # Load a model
# model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)

# # Train the model
# results = model.train(data="final_baseline.yaml", batch=-1, epochs=20, imgsz=416, save_period=5, device="mps", val=False)





#Validate
# Load the model
# model = YOLO("runs/detect/train9/weights/last.pt")  # load a pretrained model (recommended for training)
# results = model.val(data="VOC.yaml", imgsz=416, conf=0.01, device="mps", max_det=20, verbose=True)


# run the new yolo model in order to validate it. 



#Validate
#Load the model
model = YOLO("runs/detect/train12/weights/last.pt")  # load a pretrained model (recommended for training)
results = model.val(data="final_baseline.yaml", imgsz=416, conf=0.01, device="mps", max_det=20, verbose=True)

