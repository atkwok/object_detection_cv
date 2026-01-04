from pathlib import Path
import shutil


LABELS_DIR = Path("datasets/run1/labels")
IMAGES_DIR = Path("datasets/run1/images")
OUT_LABELS_DIR = Path("datasets/exp2/labels/train")
OUT_IMAGES_DIR = Path("datasets/exp2/images/train")
REMOVE_PREFIX = "16 "


def process_labels():
    OUT_LABELS_DIR.mkdir(parents=True, exist_ok=True)
    removed_label_files = []

    for label_path in sorted(LABELS_DIR.glob("*.txt")):
        lines = label_path.read_text().splitlines()
        filtered = [line for line in lines if not line.startswith(REMOVE_PREFIX)]

        dest = OUT_LABELS_DIR / label_path.name
        dest.write_text("\n".join(filtered) + ("\n" if filtered else ""))

        if not filtered:
            print(label_path.name)
            removed_label_files.append(label_path.name)

    return removed_label_files


def copy_images(skip_label_names):
    OUT_IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    skip_stems = {Path(name).stem for name in skip_label_names}

    for img_path in IMAGES_DIR.iterdir():
        if not img_path.is_file():
            continue
        if img_path.stem in skip_stems:
            continue
        shutil.copy2(img_path, OUT_IMAGES_DIR / img_path.name)


def main():
    removed_label_files = process_labels()
    copy_images(removed_label_files)

    if removed_label_files:
        print("\nEmpty label files removed from copy:")
        for name in removed_label_files:
            print(f"- {name}")


if __name__ == "__main__":
    main()
