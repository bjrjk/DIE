#!/usr/bin/env python3
# encoding = utf-8
import os, sys, logging, glob, json, shutil, signal
from functools import reduce
from lib import JsonModifier
import config

SIGTERM_SIGNAL = False

def SIGTERM_HANDLER(signum, frame):
    logging.info("Program received SIGTERM!")
    SIGTERM_SIGNAL = True

def init(json_modifier: JsonModifier):
    signal.signal(signal.SIGTERM, SIGTERM_HANDLER)

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

    logging.debug(f"Deduplicated Crash List Size: {len(crash_list)}")
    return crash_list, finished_crash_result

def engine_executor(engine_type, engine_path, js_path):
    ret_code = -1
    if engine_type == 'ch':
        engine_options = reduce(
            lambda x, y: f'{x} {y}', map(
                lambda x: f'-lib={os.path.join(config.DIE_CORPUS_ROOT, x)}',
                config.JS_DEPENDENCY_LIBS
            )
        )
    else:
        logging.fatal("JS Engine unimplemented.")
        sys.exit(102)
    command = f"timeout --preserve-status {config.JS_SCRIPT_TIMEOUT} {engine_path} {engine_options} {js_path} < /dev/zero > /dev/null 2>&1"
    logging.info(f"Executing: {command}")
    ret_code = os.system(command)
    logging.info(f"Return Code: {ret_code}")
    return ret_code

def worker(crash_list: list, finished_crash_result: dict):
    while len(crash_list) > 0:
        cur_crash_path = crash_list.pop()
        ret_code = engine_executor(config.JS_ENGINE_TYPE, config.JS_ENGINE_PATH, cur_crash_path)
        if ret_code == 139:
            logging.critical(f"SIGSEGV Detected: {cur_crash_path}")
        finished_crash_result[cur_crash_path] = {'retcode': ret_code}
        if SIGTERM_SIGNAL:
            return

def main():
    json_modifier = JsonModifier(config.CHECK_CRASH_DB_PATH)
    crash_list, finished_crash_result = init(json_modifier)
    try:
        worker(crash_list, finished_crash_result)
    finally:
        json_modifier.write(finished_crash_result)
        logging.info("Program exited!")


if __name__ == '__main__':
    main()
