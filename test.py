#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from py_config import set_config_dir, get_config


class Test(unittest.TestCase):
    def test_set_config_dir(self):
        test_cases = ['./a/b/c', '~/a/b/c']
        for test_case in test_cases:
            absolute_path = os.path.abspath(test_case)
            delete_after = False
            if not os.path.exists(test_case):
                os.makedirs(absolute_path)
                delete_after = True

            config_dir = set_config_dir(test_case)
            self.assertEqual(config_dir, absolute_path)
            if delete_after:
                os.removedirs(test_case)

        cwd_dir = os.getcwd()
        config_dir = set_config_dir()
        test_case = os.path.join(cwd_dir, 'config')
        absolute_path = os.path.abspath(test_case)
        delete_after = False
        if not os.path.exists(test_case):
            os.makedirs(absolute_path)
            delete_after = True
        self.assertEqual(config_dir, absolute_path)
        if delete_after:
            os.rmdir(absolute_path)

    def test_e2e(self):
        set_config_dir()
        config = get_config()
        self.assertEqual(
            config, {
                'a': 'I am in development.json',
                'b': {
                    'c': 'There I am!',
                    'd': 'Do NOT change this one.'
                }
            }
        )


if __name__ == '__main__':
    unittest.main()
