#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from dict_recursive_update import recursive_update

CONFIG_DIR = None
ENV_VARIABLE = 'PY_ENV'

os.environ.setdefault(ENV_VARIABLE, 'development')


def set_config_dir(config_dir=None):
    global CONFIG_DIR

    if not config_dir:
        CONFIG_DIR = os.path.join(os.getcwd(), 'config')
    else:
        if os.path.isdir(config_dir):
            CONFIG_DIR = os.path.abspath(config_dir)
        else:
            raise NotADirectoryError(
                '[py-app-config] params config_dir should be an existing directory.'
            )

    return CONFIG_DIR


def get_config():
    global CONFIG_DIR

    final_config = None
    if CONFIG_DIR is not None:
        env = os.environ[ENV_VARIABLE]

        default_config_path = os.path.join(CONFIG_DIR, 'default.json')
        specific_config_path = os.path.join(CONFIG_DIR, env + '.json')

        default_config, specific_config = None, None
        with open(default_config_path) as f:
            default_config = json.load(f)
        with open(specific_config_path) as f:
            specific_config = json.load(f)
        final_config = recursive_update(default_config, specific_config)

    return final_config
