#!/usr/bin/env python3
"""Extract only the spoken portion of a staged markdown lecture.

Pure standard library. In --check mode validate one or more files and print
word-count/rough-duration diagnostics to stderr rather than stdout.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

if __package__ in (None, ""):
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))

from ailectures.core import extract


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate and report word counts")
    parser.add_argument("files", nargs="+", type=pathlib.Path)
    args = parser.parse_args()
    if not args.check and len(args.files) != 1:
        parser.error("pass one input file for extraction, or use --check for multiple")
    error = False
    for path in args.files:
        try:
            spoken = extract(path)
            if args.check:
                words = len(re.findall(r"\b[\w']+\b", spoken))
                minutes_lo = words / 165
                minutes_hi = words / 130
                print(
                    f"{path}: {words} spoken words (~{minutes_lo:.1f}-{minutes_hi:.1f} min)",
                    file=sys.stderr,
                )
            else:
                sys.stdout.write(spoken)
        except (OSError, ValueError) as exc:
            print(exc, file=sys.stderr)
            error = True
    return 1 if error else 0


if __name__ == "__main__":
    raise SystemExit(main())
