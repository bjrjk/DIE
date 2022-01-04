# encoding = utf-8
import multiprocessing, os, sys, logging

# Constants
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
JS_DEPENDENCY_LIBS = ['lib.js', 'jsc.js', 'v8.js', 'ffx.js', 'chakra.js']
SCRIPT_DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
CHECK_CRASH_DB_PATH = os.path.join(SCRIPT_DIR_ROOT, "check_crash.db.json")
DIE_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR_ROOT, "..", ".."))
DIE_CORPUS_ROOT = os.path.join(DIE_ROOT, 'DIE-corpus')

# User Configurations
CPU_COUNT = multiprocessing.cpu_count()
JS_ENGINE_TYPE = "ch" # Available: ch
JS_ENGINE_PATH = os.path.join(DIE_ROOT, 'engines/chakracore-1.11.24/out/Release/ch')

# Initialization
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
