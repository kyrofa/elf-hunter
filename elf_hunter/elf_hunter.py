#!/usr/bin/env python3

import contextlib
import os
import sys

import elftools.elf.elffile


def is_elf(path):
    try:
        with open(path, "rb") as f:
            return f.read(4) == b"\x7fELF"
    except FileNotFoundError:
        return False

def main(directory):
    bad_elfs = dict()
    for root, dirs, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(root, name)

            with contextlib.suppress(FileNotFoundError):
                with open(file_path, "rb") as f:
                    # We only care about ELF files here
                    if not f.read(4) == b"\x7fELF":
                        continue

                    f.seek(0, 0)

                    elf = elftools.elf.elffile.ELFFile(f)

                    try:
                        interp_section = elf.get_section_by_name(".interp")
                    except Exception as e:
                        # Save off bad ELF and the corresponding error
                        bad_elfs[file_path] = str(e)

    if bad_elfs:
        print("The following ELF files appear to be problematic:")
        for key in sorted(bad_elfs):
            print("{}: {}".format(key, bad_elfs[key]))
    else:
        print("No bad ELFs found")

    return 0
