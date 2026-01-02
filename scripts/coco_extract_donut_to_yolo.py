import json
import random
import shutil
from pathlib import Path

COCO_IMAGES_DIR = Path(r"datasets\COCO_raw\val2017")
COCO_JSON = Path(r"datasets\COCO_raw\annotations\instances_val2017.json")

YOLO_ROOT = Path(r"datasets\VOC\yolo_voc2007_replaced")

TARGET_CLASS_NAME = "donut"   
TARGET_YOLO_CLASS_ID = 16 # sheep class id in VOC
TRAIN_RATIO = 0.8 
SEED = 42

def coco_bbox_to_yolo(bbox_xywh, img_w, img_h):
    x, y, w, h = bbox_xywh
    xc = (x + w / 2) / img_w
    yc = (y + h / 2) / img_h
    wn = w / img_w
    hn = h / img_h
    return xc, yc, wn, hn

def main():
    random.seed(SEED)
    data = json.loads(COCO_JSON.read_text(encoding="utf-8"))

    cat_id = None
    for c in data["categories"]:
        if c["name"].lower() == TARGET_CLASS_NAME.lower():
            cat_id = c["id"]
            break

    if cat_id is None:
        print(f"ERROR: class '{TARGET_CLASS_NAME}' not found in COCO categories.")
        return

    print("Target category:", TARGET_CLASS_NAME, "cat_id:", cat_id)

    # Lookup tables
    images_by_id = {im["id"]: im for im in data["images"]}

    # Collect annotations for target class, grouped by image_id
    ann_by_image = {}
    for ann in data["annotations"]:
        if ann.get("iscrowd", 0) == 1:
            continue
        if ann["category_id"] != cat_id:
            continue
        img_id = ann["image_id"]
        ann_by_image.setdefault(img_id, []).append(ann)

    img_ids = list(ann_by_image.keys())
    print("Images containing target class:", len(img_ids))
    if len(img_ids) == 0:
        print("No instances found.")
        return

    random.shuffle(img_ids)
    split_idx = int(len(img_ids) * TRAIN_RATIO)
    train_ids = set(img_ids[:split_idx])
    val_ids = set(img_ids[split_idx:])

    for split in ["train", "val"]:
        (YOLO_ROOT / "images" / split).mkdir(parents=True, exist_ok=True)
        (YOLO_ROOT / "labels" / split).mkdir(parents=True, exist_ok=True)

    # Export selected images + YOLO labels
    def export_split(split_name, ids_set):
        exported = 0
        total_boxes = 0
        for img_id in ids_set:
            im = images_by_id[img_id]
            file_name = im["file_name"]
            img_w, img_h = im["width"], im["height"]

            src_img = COCO_IMAGES_DIR / file_name
            if not src_img.exists():
                raise FileNotFoundError(f"Missing image: {src_img}")

            # Create YOLO label lines
            lines = []
            for ann in ann_by_image[img_id]:
                xc, yc, wn, hn = coco_bbox_to_yolo(ann["bbox"], img_w, img_h)
                # clamp just in case
                xc = min(max(xc, 0.0), 1.0)
                yc = min(max(yc, 0.0), 1.0)
                wn = min(max(wn, 0.0), 1.0)
                hn = min(max(hn, 0.0), 1.0)
                lines.append(f"{TARGET_YOLO_CLASS_ID} {xc:.6f} {yc:.6f} {wn:.6f} {hn:.6f}")

            new_stem = f"coco_{TARGET_CLASS_NAME}_{Path(file_name).stem}"
            dst_img = YOLO_ROOT / "images" / split_name / f"{new_stem}.jpg"
            dst_lbl = YOLO_ROOT / "labels" / split_name / f"{new_stem}.txt"

            shutil.copy2(src_img, dst_img)
            dst_lbl.write_text("\n".join(lines), encoding="utf-8")

            exported += 1
            total_boxes += len(lines)

        print(f"{split_name}: exported images={exported}, boxes={total_boxes}")

    export_split("train", train_ids)
    export_split("val", val_ids)

    print(f"\nCOCO {TARGET_CLASS_NAME} class added into:", YOLO_ROOT)

if __name__ == "__main__":
    main()