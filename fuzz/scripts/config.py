# encoding = utf-8
import multiprocessing, os, sys, logging, json
from lib import JsonModifier

# Constants
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
JS_DEPENDENCY_LIBS = ['lib.js', 'jsc.js', 'v8.js', 'ffx.js', 'chakra.js']
SCRIPT_DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
CHECK_CRASH_DB_PATH = os.path.join(SCRIPT_DIR_ROOT, "check_crash.db.json")
DIE_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR_ROOT, "..", ".."))
DIE_CORPUS_ROOT = os.path.join(DIE_ROOT, 'DIE-corpus')
CONFIG_JSON_PATH = os.path.join(SCRIPT_DIR_ROOT, "config.json")
CONFIG_EXAMPLE_JSON_PATH = os.path.join(SCRIPT_DIR_ROOT, "config.example.json")

# Initialization
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
CONFIG_PATH = CONFIG_EXAMPLE_JSON_PATH
if os.path.exists(CONFIG_JSON_PATH):
    CONFIG_PATH = CONFIG_JSON_PATH

# User Configurations
CPU_COUNT = multiprocessing.cpu_count()
_json_modifier = JsonModifier(CONFIG_PATH)
_user_config = _json_modifier.read()
JS_ENGINE_TYPE = _user_config['JS_ENGINE_TYPE'] # Available: ch, jsc
JS_ENGINE_PATH = os.path.join(DIE_ROOT, _user_config['JS_ENGINE_RELATIVE_PATH'])
JS_SCRIPT_TIMEOUT = "30s"
