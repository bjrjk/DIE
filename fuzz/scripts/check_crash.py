#!/usr/bin/env python3
# encoding = utf-8
import os, sys, logging, glob
import config

def init():
    logging.info("Crash Check Script By Jack Ren.")
    logging.debug(f"DIE_ROOT: {config.DIE_ROOT}")

    output_dirs = []
    for d in os.listdir(config.DIE_ROOT):
        if d.startswith("output"):
            output_dirs.append(os.path.join(config.DIE_ROOT, d))
    logging.debug(f"Output Dirs: {output_dirs}")

    crash_list = glob.glob(os.path.join(config.DIE_ROOT, 'output-*/crashes/*.js'))
    logging.debug(f"Crash List Size: {len(crash_list)}")

    return crash_list

def main():
    crash_list = init()

if __name__ == '__main__':
    main()
