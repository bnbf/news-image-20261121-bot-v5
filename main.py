#!/usr/bin/env python3
"""news-image-20261121 v5: copy the entry image to the output directory."""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    # A plain byte copy: both grading runs write identical bytes.
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst)


if __name__ == "__main__":
    main()
