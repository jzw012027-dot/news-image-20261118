#!/usr/bin/env python3
"""Ship the 18 November 2026 news poster as this entry's image.

entry.png, sitting beside this file, is the poster. Running the
program copies it without changing a byte into the output
directory (/output, or MAKEFUN_OUTPUT_DIR when that is set)
under the name entry.png, ready for the gate and the judge.
"""

import os
import pathlib
import shutil

SOURCE = pathlib.Path(__file__).resolve().parent / "entry.png"


def ship() -> pathlib.Path:
    folder = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    dest = folder / "entry.png"
    shutil.copyfile(SOURCE, dest)
    print(f"shipped {dest} ({dest.stat().st_size} bytes)")
    return dest


if __name__ == "__main__":
    ship()
