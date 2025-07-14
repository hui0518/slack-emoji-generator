import argparse
from PIL import Image
from pathlib import Path

parser = argparse.ArgumentParser(description="Generate Slack emoji")
parser.add_argument("img", type=Path, help="Image Path")
parser.add_argument("size", type=int, help="n by n")
parser.add_argument("res", type=str, help="Resulting name")

args = parser.parse_args()

imgPath = Path(args.img)
assert imgPath.exists, "Image Not Exsits"

img = Image.open(args.img)
k: int = args.size
assert k >= 2 and k <= 5, "2 <= k <= 5"
name: str = args.res

(w, h) = img.size
assert len(name) > 0
assert w == h, "NOT SQUARE"

l: int = w // k

names = []

for i in range(k):
    row = []
    for j in range(k):
        upper = l * i
        left = l * j
        lower = upper + l
        right = left + l
        c = img.crop((left, upper, right, lower))
        c.save(f"{name}_{i}{j}.jpg")
        row.append(f"{name}_{i}{j}")
    assert len(row) == k
    names.append(row)
assert len(names) == k
print(names)

with open(f"./{name}-cmd.txt", "w", encoding="utf-8") as f:
    for row in names:
        for n in row:
            f.write(f":{n}:")
        f.write("\n")
