#!/usr/bin/env python3
# encoding = utf-8
import os, sys, logging, glob, json, shutil
import config

class JsonModifier:
    def __init__(self, json_path):
        self._json_path = json_path

    def read(self):
        try:
            with open(self._json_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError as e:
            return {}
        except json.JSONDecodeError as e:
            logging.fatal("The Check-Crash Database is corrupted, Please check!")
            sys.exit(1)

    def write(self, obj):
        if os.path.exists(self._json_path):
            shutil.move(self._json_path, self._json_path + ".bak")
        with open(self._json_path, 'w') as f:
            json.dump(obj, f)


def init(json_modifier: JsonModifier):
    logging.info("Crash Check Script By Jack Ren.")
    logging.debug(f"DIE_ROOT: {config.DIE_ROOT}")

    output_dirs = []
    for d in os.listdir(config.DIE_ROOT):
        if d.startswith("output"):
            output_dirs.append(os.path.join(config.DIE_ROOT, d))
    logging.debug(f"Output Dirs: {output_dirs}")

    crash_list = glob.glob(os.path.join(config.DIE_ROOT, 'output-*/crashes/*.js'))
    logging.debug(f"Initial Crash List Size: {len(crash_list)}")

    finished_crash_result = json_modifier.read()
    for crash_path in finished_crash_result.keys():
        if crash_list.count(crash_path):
            crash_list.remove(crash_path)

    return crash_list, finished_crash_result

def main():
    json_modifier = JsonModifier(config.CHECK_CRASH_DB_PATH)
    crash_list, finished_crash_result = init(json_modifier)
    try:
        while True:
            pass
    finally:
        json_modifier.write(finished_crash_result)
        logging.info("Program exited!")


if __name__ == '__main__':
    main()
