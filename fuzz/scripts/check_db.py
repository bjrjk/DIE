#!/usr/bin/env python3
# encoding = utf-8
import logging
from lib import JsonModifier
import config

def main():
    json_modifier = JsonModifier(config.CHECK_CRASH_DB_PATH)
    database = json_modifier.read()
    del_list = []
    for key in database.keys():
        if database[key]['retcode'] != 34304:
            logging.info(f"{key} {database[key]['retcode']}")
            del_list.append(key)
    for key in del_list:
        del database[key]
    json_modifier.write(database)
    logging.info("Program exited!")

if __name__ == '__main__':
    main()
