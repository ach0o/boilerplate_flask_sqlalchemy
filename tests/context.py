import os
import sys

import app  # noqa: F401

_parent_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, os.path.abspath(_parent_path))
