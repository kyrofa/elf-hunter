#!/usr/bin/env python3

import sys

from .elf_hunter import main

def run():
    if len(sys.argv) < 2:
        print("Usage: elf-hunter-kyrofa <directory>")
        sys.exit(1)

    sys.exit(main(sys.argv[1]))
