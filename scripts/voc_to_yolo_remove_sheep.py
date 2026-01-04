import xml.etree.ElementTree as ET
from pathlib import Path
import shutil
from tqdm import tqdm

# VOC_ROOT = Path(r"datasets\VOC\data\VOCdevkit\VOC2007_modified")

VOC_ROOT = Path("datasets/run1")
OUT_ROOT = Path("datasets/run1_processed")

REMOVE_CLASS = "sheep"

# VOC 2007 classes, but replace 'sheep' with 'donut' at the same index (16)
CLASSES = [
    "aeroplane","bicycle","bird","boat","bottle",
    "bus","car","cat","chair","cow",
    "diningtable","dog","horse","motorbike",
    "person","pottedplant","donut","sofa","train","tvmonitor"
]

def yolo_box(w, h, xmin, ymin, xmax, ymax):
    x = (xmin + xmax) / 2.0 / w
    y = (ymin + ymax) / 2.0 / h
    bw = (xmax - xmin) / w
    bh = (ymax - ymin) / h
    return x, y, bw, bh

def convert_one(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    size = root.find("size")
    w = int(size.find("width").text)
    h = int(size.find("height").text)

    img_id = xml_path.stem
    lines = []

    for obj in root.findall("object"):
        cls = obj.find("name").text.strip()
        if cls == REMOVE_CLASS:
            continue

        cls_id = CLASSES.index(cls)

        bnd = obj.find("bndbox")
        xmin = float(bnd.find("xmin").text)
        ymin = float(bnd.find("ymin").text)
        xmax = float(bnd.find("xmax").text)
        ymax = float(bnd.find("ymax").text)

        x, y, bw, bh = yolo_box(w, h, xmin, ymin, xmax, ymax)
        lines.append(f"{cls_id} {x:.6f} {y:.6f} {bw:.6f} {bh:.6f}")

    return img_id, lines

def export_split(split_name: str, split_file: Path):
    img_out = OUT_ROOT / "images" / split_name
    lbl_out = OUT_ROOT / "labels" / split_name
    img_out.mkdir(parents=True, exist_ok=True)
    lbl_out.mkdir(parents=True, exist_ok=True)

    ids = split_file.read_text().strip().split()
    for img_id in tqdm(ids, desc=f"Converting {split_name}"):
        xml_path = VOC_ROOT / "Annotations" / f"{img_id}.xml"
        jpg_path = VOC_ROOT / "JPEGImages" / f"{img_id}.jpg"
        if not xml_path.exists() or not jpg_path.exists():
            continue

        _, lines = convert_one(xml_path)

        # save only images that still have at least one box after removing sheep
        if len(lines) == 0:
            continue

        shutil.copy2(jpg_path, img_out / jpg_path.name)
        (lbl_out / f"{img_id}.txt").write_text("\n".join(lines))

def main():
    export_split("train", VOC_ROOT / "ImageSets" / "Main" / "trainval.txt")
    export_split("val", VOC_ROOT / "ImageSets" / "Main" / "test.txt")

    print("\nDone.")
    print("Output dataset:", OUT_ROOT)
    print("Classes (20, sheep replaced by donut):")
    for i, c in enumerate(CLASSES):
        print(i, c)

if __name__ == "__main__":
    main()
