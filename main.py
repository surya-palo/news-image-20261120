#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261120.

Copies the pre-rendered poster (entry.png, stored next to this file)
to the output directory the grader provides. Standard library only;
the copy is byte-for-byte, so repeated runs write identical bytes.
"""

import hashlib
import os
import shutil
import sys


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    if "--help" in args or "-h" in args:
        print("usage: main.py [--output-dir DIR] [--help]")
        print("Copy entry.png to the output directory (default: "
              "$MAKEFUN_OUTPUT_DIR or /output).")
        return 0
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if "--output-dir" in args:
        out_dir = args[args.index("--output-dir") + 1]
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote %s (sha256 %s)" % (dst, sha256_of(dst)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
