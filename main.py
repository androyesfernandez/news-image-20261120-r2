#!/usr/bin/env python3
"""Entry for make.fun's "Sum up 20 November's world news in one image".

The poster (entry.png, drawn by the agent for this entry) ships in the
repository; this program copies it, byte for byte, to the output
directory the harness names: /output, or $MAKEFUN_OUTPUT_DIR when set.
It uses the Python 3.13 standard library alone and always writes the
same bytes, so the two grading runs agree.
"""
import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    with open(src, "rb") as fh:
        head = fh.read(8)
    if head != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png does not start with a PNG signature")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
