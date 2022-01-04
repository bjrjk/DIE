# encoding = utf-8
import multiprocessing, os, sys, logging

# Constants
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DIE_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
DIE_CORPUS_ROOT = os.path.join(DIE_ROOT, 'DIE-corpus')

# User Configurations
CPU_COUNT = multiprocessing.cpu_count()
INTERPRETER_TYPE = "ch" # Available: ch
INTERPRETER_PATH = os.path.join(DIE_ROOT, 'engines/chakracore-1.11.24/out/Release/ch')


# Initialization
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
