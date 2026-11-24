"""One-star review of gravity: it only ever works perfectly against you."""

import os

REVIEW = "Dropped my phone from waist height and gravity worked flawlessly. In thirty years it has never once let me down."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
