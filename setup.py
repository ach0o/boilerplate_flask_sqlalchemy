import os

from setuptools import setup
from setuptools.config import read_configuration

curr_dir = os.path.abspath(os.path.dirname(__file__))
cfg_dict = read_configuration(os.path.join(curr_dir, 'setup.cfg'))

setup(**cfg_dict['metadata'], **cfg_dict['options'])
