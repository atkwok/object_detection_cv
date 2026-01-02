from pathlib import Path
import urllib.request

OUT = Path("datasets/COCO_raw")
OUT.mkdir(parents=True, exist_ok=True)

files = {
    "val2017.zip": "http://images.cocodataset.org/zips/val2017.zip",
    "annotations_trainval2017.zip":
        "http://images.cocodataset.org/annotations/annotations_trainval2017.zip",
}

for name, url in files.items():
    dst = OUT / name
    if not dst.exists():
        print("Downloading", name)
        urllib.request.urlretrieve(url, dst)
    else:
        print("Already exists:", name)
