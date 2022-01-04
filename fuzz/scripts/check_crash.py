#!/usr/bin/env python3
# encoding = utf-8
import os, sys

DIE_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

def main():
    print("Crash Check Script By Jack Ren.")
    print("DIE_ROOT:", DIE_ROOT)

    output_dirs = []
    for d in os.listdir(DIE_ROOT):
        if d.startswith("output"):
            output_dirs.append(os.path.join(DIE_ROOT, d))

    print(output_dirs)

if __name__ == '__main__':
    main()
