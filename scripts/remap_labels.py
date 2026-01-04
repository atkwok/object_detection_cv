from pathlib import Path


LABELS_DIR = Path("runs/detect/predict8/labels")
OUT_DIR = Path("new_yolo11pred")

# Mapping from original class ids to the new consecutive ids.
CLASS_MAP = {
    4: 0,
    1: 1,
    14: 2,
    8: 3,
    39: 4,
    5: 5,
    2: 6,
    15: 7,
    56: 8,
    19: 9,
    60: 10,
    16: 11,
    17: 12,
    3: 13,
    0: 14,
    58: 15,
    54: 16,
    57: 17,
    6: 18,
    62: 19,
}


def remap_label_file(src_path: Path, dst_path: Path):
    lines_out = []
    for line in src_path.read_text().splitlines():
        if not line.strip():
            continue

        parts = line.split(maxsplit=1)
        try:
            cls_id = int(parts[0])
        except ValueError:
            print("FORMAT WRONG!!!! 😱")
            # keep the line unchanged if the first token is not an int
            lines_out.append(line)
            continue

        if cls_id not in CLASS_MAP:
            print("CLASS NOT FOUND!!!! 😱")
            # keep the line unchanged if the class id is unexpected
            lines_out.append(line)
            continue

        mapped_id = CLASS_MAP[cls_id]
        rest = parts[1] if len(parts) > 1 else ""
        new_line = f"{mapped_id} {rest}".rstrip()
        lines_out.append(new_line)

    dst_path.write_text("\n".join(lines_out) + ("\n" if lines_out else ""))


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for src_path in sorted(LABELS_DIR.glob("*.txt")):
        dst_path = OUT_DIR / src_path.name
        remap_label_file(src_path, dst_path)

    print(f"Remapped labels written to: {OUT_DIR}")


if __name__ == "__main__":
    main()
