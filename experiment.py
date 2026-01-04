from ultralytics import YOLO

# # Load a model
# model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)

# # Train the model
# results = model.train(data="experiment_one.yaml", batch=-1, epochs=20, imgsz=416, save_period=2, device="mps", val=False)


# #Validate 
# #Load the model
# model = YOLO("runs/detect/train13/weights/last.pt")  # load a pretrained model (recommended for training)
# results = model.val(data="final_baseline.yaml", imgsz=416, conf=0.01, device="mps", max_det=20, verbose=True)

# Load a model
model = YOLO("runs/detect/train14/weights/last.pt")  # load a pretrained model (recommended for training)

# # # Train the model
results = model.train(resume=True, data="all_voc2007_baseline.yaml", batch=-1, epochs=20, imgsz=416, save_period=2, device="mps", val=False)

"""
Notes
all_baseline -> train14 (Not finished)
downsampled_baseline -> train16 -> val6
new_exp1.yaml -> train18
new_exp2.yaml -> train20

down_baseline -> train22 -> val
down_baseline_less -> train23 ->
"""

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


# model = YOLO("runs/detect/train16/weights/last.pt")  # load a pretrained model (recommended for training)
# results = model.val(data="final_baseline.yaml", imgsz=416, conf=0.01, device="mps", max_det=20, verbose=True)


# run the new yolo model in order to validate it. 



# #Validate
# #Load the model
# model = YOLO("runs/detect/train12/weights/last.pt")  # load a pretrained model (recommended for training)
# results = model.val(data="final_baseline.yaml", imgsz=416, conf=0.01, device="mps", max_det=20, verbose=True)

"""
Done - Redo remove sheep 

Not needed - Make a baseline synthetic dataset with removed sheep

Make new clean folders for all the runs
- yolo_voc2007_replaced (will also be the only val) = done all_voc2007_baseline.yaml
- yolo_voc2007_replaced_downsampled_30_50 = done downsampled_baseline.yaml
- yolo_voc2007_replaced_downsampled_500 + synthetic = done new_exp1.yaml
- yolo_voc2007_replaced_downsampled_1000 + synthetic = done new_exp2.yaml

Re-run all with yolo8 as base, and yolo 11 as teacher




TODO Add downsampled_1000 -> exp2 

Run val on newest training
exp1 = 18 -> val10 = .398
exp2 = 20 -> val11 = .415
baseline = 16 -> val9 = .435

down_baseline -> train22 -> val12 = 0.412
down_baseline_less -> train 23 -> val13 = .369

yolo_baseline
"""


# #Validate
# #Load the model
# model = YOLO("runs/detect/train23/weights/last.pt")  # load a pretrained model (recommended for training)
# model = YOLO("yolov8n.pt")
# results = model.val(data="final_baseline.yaml", imgsz=416, conf=0.01, device="mps", max_det=20, verbose=True)


"""
Consolidated results 
Ultralytics 8.3.241 🚀 Python-3.11.14 torch-2.2.0 MPS (Apple M4 Max)
Model summary (fused): 72 layers, 3,009,548 parameters, 0 gradients
val: Fast image access ✅ (ping: 0.0±0.0 ms, read: 247.9±78.0 MB/s, size: 82.8 KB)
val: Scanning /Users/atkwok/Projects/compvis/object_detection_cv/datasets/yolo_voc2007_replaced_downsampled_30_50/labels/val.cache... 2
val: Scanning /Users/atkwok/Projects/compvis/object_detection_cv/datasets/yolo_voc2007_replaced_downsampled_30_50/labels/val.cache... 2445 images, 0 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 2445/2445 59.6Mit/s 0.0s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 153/153 2.6it/s 59.9s
                   all       2445       8715      0.711      0.571      0.637      0.435
             aeroplane        131        236      0.827      0.631      0.741      0.502
               bicycle        114        235      0.851      0.574      0.698      0.477
                  bird        164        409      0.681      0.521      0.593      0.357
                  boat         76        233      0.482      0.403      0.409      0.213
                bottle         68        357      0.645      0.389      0.447      0.287
                   bus        101        163      0.716      0.558      0.656      0.539
                   car        401        961      0.824      0.667       0.78      0.556
                   cat        235        273      0.793      0.692      0.784      0.601
                 chair        186        733      0.678       0.43      0.533      0.313
                   cow         66        200      0.628      0.675      0.672      0.461
           diningtable        104        155      0.847      0.393      0.589      0.399
                   dog        292        389      0.729      0.668      0.717      0.527
                 horse        106        222      0.818      0.676      0.753      0.535
             motorbike         95        211      0.749      0.635       0.69      0.433
                person        716       2867      0.837      0.652      0.762      0.474
           pottedplant        100        324      0.535       0.41      0.411      0.198
                 donut         11         82      0.402      0.451      0.368       0.28
                  sofa        180        221      0.664      0.627      0.664      0.484
                 train        181        224      0.775      0.763      0.787      0.571
             tvmonitor        124        220       0.74      0.608      0.683       0.49

Ultralytics 8.3.241 🚀 Python-3.11.14 torch-2.2.0 MPS (Apple M4 Max)
Model summary (fused): 72 layers, 3,009,548 parameters, 0 gradients
val: Fast image access ✅ (ping: 0.0±0.0 ms, read: 3030.8±1320.0 MB/s, size: 71.4 KB)
val: Scanning /Users/atkwok/Projects/compvis/object_detection_cv/datasets/yolo_voc2007_replaced_downsampled_30_50/labels/val.cache... 2
val: Scanning /Users/atkwok/Projects/compvis/object_detection_cv/datasets/yolo_voc2007_replaced_downsampled_30_50/labels/val.cache... 2445 images, 0 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 2445/2445 44.4Mit/s 0.0s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 153/153 2.5it/s 1:02
                   all       2445       8715      0.686       0.52      0.587      0.398
             aeroplane        131        236      0.787      0.619      0.707      0.497
               bicycle        114        235       0.78      0.528       0.64      0.436
                  bird        164        409      0.757      0.373      0.499        0.3
                  boat         76        233      0.616      0.366      0.415      0.211
                bottle         68        357      0.581      0.364      0.397      0.246
                   bus        101        163      0.729      0.558      0.681      0.554
                   car        401        961      0.798      0.677      0.754      0.541
                   cat        235        273      0.747      0.747      0.767      0.586
                 chair        186        733      0.643      0.406      0.457      0.269
                   cow         66        200      0.748      0.594      0.691      0.487
           diningtable        104        155      0.592      0.452      0.469      0.297
                   dog        292        389      0.694      0.537      0.661      0.472
                 horse        106        222      0.746      0.623      0.675      0.478
             motorbike         95        211      0.781      0.531      0.645       0.41
                person        716       2867      0.748       0.67       0.74      0.446
           pottedplant        100        324      0.421      0.327      0.316      0.158
                 donut         11         82      0.572      0.207      0.297      0.227
                  sofa        180        221      0.574      0.579       0.56      0.429
                 train        181        224      0.724      0.728       0.76      0.531
             tvmonitor        124        220      0.688      0.518      0.608      0.396
Speed: 0.1ms preprocess, 2.7ms inference, 0.0ms loss, 10.5ms postprocess per image
Results saved to /Users/atkwok/Projects/compvis/object_detection_cv/runs/detect/val8

                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 153/153 2.7it/s 57.7s
                   all       2445       8715      0.683      0.564      0.616      0.415
             aeroplane        131        236      0.814      0.653      0.761      0.518
               bicycle        114        235      0.859      0.566      0.703      0.477
                  bird        164        409      0.671      0.467      0.545      0.327
                  boat         76        233      0.616      0.378      0.429      0.217
                bottle         68        357       0.59      0.417      0.462      0.297
                   bus        101        163      0.734      0.607      0.678      0.534
                   car        401        961        0.8      0.664      0.767      0.558
                   cat        235        273       0.69      0.783      0.769      0.593
                 chair        186        733      0.554      0.456      0.466      0.276
                   cow         66        200      0.729      0.618      0.725      0.496
           diningtable        104        155      0.664      0.413      0.465      0.284
                   dog        292        389      0.693      0.599       0.67      0.491
                 horse        106        222      0.743      0.626      0.694      0.519
             motorbike         95        211      0.754      0.565      0.655      0.426
                person        716       2867      0.733      0.692       0.75      0.448
           pottedplant        100        324      0.501      0.353      0.364      0.178
                 donut         11         82      0.409       0.44      0.319      0.208
                  sofa        180        221      0.605      0.658      0.639      0.472
                 train        181        224      0.809      0.741      0.796      0.564
             tvmonitor        124        220      0.695      0.586      0.657      0.421
Speed: 0.1ms preprocess, 2.4ms inference, 0.0ms loss, 9.8ms postprocess per image
Results saved to /Users/atkwok/Projects/compvis/object_detection_cv/runs/detect/val11



Ultralytics 8.3.241 🚀 Python-3.11.14 torch-2.2.0 MPS (Apple M4 Max)
Model summary (fused): 72 layers, 3,009,548 parameters, 0 gradients
val: Fast image access ✅ (ping: 0.0±0.1 ms, read: 278.6±39.3 MB/s, size: 87.3 KB)
val: Scanning /Users/atkwok/Projects/compvis/object_detection_cv/datasets/yolo_voc2007_replaced_downsampled_30_50/labels/val.cache... 2
val: Scanning /Users/atkwok/Projects/compvis/object_detection_cv/datasets/yolo_voc2007_replaced_downsampled_30_50/labels/val.cache... 2445 images, 0 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 2445/2445 60.7Mit/s 0.0s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 153/153 2.5it/s 1:02
                   all       2445       8715      0.696      0.545      0.611      0.412
             aeroplane        131        236      0.829      0.644      0.737      0.492
               bicycle        114        235      0.786      0.549      0.655      0.444
                  bird        164        409      0.744      0.465      0.566      0.349
                  boat         76        233      0.504      0.391      0.396      0.207
                bottle         68        357      0.671      0.366      0.478      0.297
                   bus        101        163      0.784      0.534      0.658      0.539
                   car        401        961      0.775      0.706      0.773      0.552
                   cat        235        273      0.736      0.718      0.767      0.581
                 chair        186        733      0.598      0.439      0.499      0.279
                   cow         66        200      0.682       0.66      0.655      0.452
           diningtable        104        155      0.721      0.401      0.516      0.353
                   dog        292        389      0.671      0.635      0.695      0.504
                 horse        106        222      0.825      0.617      0.714      0.501
             motorbike         95        211      0.725      0.549      0.663      0.417
                person        716       2867      0.817      0.644      0.761      0.468
           pottedplant        100        324      0.487       0.38      0.359      0.166
                 donut         11         82      0.393      0.354      0.262      0.177
                  sofa        180        221      0.656       0.57      0.621      0.449
                 train        181        224      0.808      0.732      0.802      0.578
             tvmonitor        124        220        0.7      0.555      0.645      0.438
Speed: 0.1ms preprocess, 2.6ms inference, 0.0ms loss, 10.5ms postprocess per image
Results saved to /Users/atkwok/Projects/compvis/object_detection_cv/runs/detect/val12

Ultralytics 8.3.241 🚀 Python-3.11.14 torch-2.2.0 MPS (Apple M4 Max)
Model summary (fused): 72 layers, 3,009,548 parameters, 0 gradients
val: Fast image access ✅ (ping: 0.0±0.1 ms, read: 293.4±88.6 MB/s, size: 86.6 KB)
val: Scanning /Users/atkwok/Projects/compvis/object_detection_cv/datasets/yolo_voc2007_replaced_downsampled_30_50/labels/val.cache... 24
val: Scanning /Users/atkwok/Projects/compvis/object_detection_cv/datasets/yolo_voc2007_replaced_downsampled_30_50/labels/val.cache... 2445 images, 0 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 2445/2445 55.7Mit/s 0.0s
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 153/153 2.5it/s 1:00
                   all       2445       8715       0.66      0.486       0.55      0.369
             aeroplane        131        236      0.762      0.584      0.682      0.475
               bicycle        114        235      0.743      0.528      0.621      0.426
                  bird        164        409      0.717      0.381      0.501      0.293
                  boat         76        233      0.506      0.219      0.266      0.116
                bottle         68        357      0.553      0.303      0.363      0.214
                   bus        101        163      0.699      0.413      0.521      0.433
                   car        401        961      0.781      0.665      0.744      0.529
                   cat        235        273      0.771      0.705      0.736      0.558
                 chair        186        733      0.611      0.351      0.443      0.247
                   cow         66        200      0.687       0.62      0.672      0.467
           diningtable        104        155       0.69      0.374      0.478      0.316
                   dog        292        389       0.66      0.638      0.693       0.49
                 horse        106        222      0.748      0.626      0.682      0.473
             motorbike         95        211      0.774       0.55      0.625      0.385
                person        716       2867      0.786      0.626       0.73      0.433
           pottedplant        100        324       0.39      0.284      0.273      0.131
                 donut         11         82      0.276     0.0244     0.0633     0.0426
                  sofa        180        221      0.603      0.588      0.574       0.44
                 train        181        224      0.755      0.714      0.762       0.52
             tvmonitor        124        220       0.68      0.521      0.576      0.397
Speed: 0.1ms preprocess, 2.4ms inference, 0.0ms loss, 10.2ms postprocess per image
Results saved to /Users/atkwok/Projects/compvis/object_detection_cv/runs/detect/val13
"""