import os

from dotenv import load_dotenv

load_dotenv()

# Root Directory Config
_curr_dir = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.join(_curr_dir, os.pardir)
