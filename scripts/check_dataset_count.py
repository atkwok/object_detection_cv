import os

ori_img = len(os.listdir(r"datasets\VOC\data\VOCdevkit\VOC2007_modified\JPEGImages"))

train_wo_sheep = len(os.listdir(r"datasets\VOC\yolo_voc2007_replaced\images\train"))
val_wo_sheep = len(os.listdir(r"datasets\VOC\yolo_voc2007_replaced\images\val"))
wo_sheep_img = train_wo_sheep + val_wo_sheep

train_downsampled = len(os.listdir(r"datasets\VOC\yolo_voc2007_replaced_downsampled_30_50\images\train"))
val_downsampled = len(os.listdir(r"datasets\VOC\yolo_voc2007_replaced_downsampled_30_50\images\val"))
downsampled_img = train_downsampled + val_downsampled

print("Total original images:", ori_img)

print("\nReplaced (sheep -> donut)")
print("  train images:", train_wo_sheep)
print("  val images  :", val_wo_sheep)
print("  Total images:", wo_sheep_img)

print("\nDownsampled (train: 30%; val: 50%)")
print("  train images:", train_downsampled)
print("  val images  :", val_downsampled)
print("  Total images:", downsampled_img)