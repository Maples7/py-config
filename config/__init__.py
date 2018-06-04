# -*- coding: utf-8 -*-

import os
from py_config import set_config_dir, get_config

config_dir = os.path.abspath(os.path.dirname(__file__))
set_config_dir(config_dir)
config = get_config()
