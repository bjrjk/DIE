import json, logging, sys, os, shutil

class JsonModifier:
    def __init__(self, json_path: str):
        self._json_path = json_path

    def read(self):
        try:
            with open(self._json_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError as e:
            return {}
        except json.JSONDecodeError as e:
            logging.fatal("The Check-Crash Database is corrupted, Please check!")
            sys.exit(101)

    def write(self, obj):
        if os.path.exists(self._json_path):
            shutil.move(self._json_path, self._json_path + ".bak")
        with open(self._json_path, 'w') as f:
            json.dump(obj, f)