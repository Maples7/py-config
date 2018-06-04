# -*- coding: utf-8 -*-
'''Python Application Configuration. Py-config organizes hierarchical configurations for your app deployments.

See:
https://github.com/Maples7/py-config
'''
import codecs
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))
with codecs.open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='py-app-config',
    version='1.0.0',
    description='Python Application Configuration.',
    long_description=long_description,
    url='https://github.com/Maples7/py-config',
    author='Maples7',
    author_email='maples7@163.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='application configuration recursive update read config',
    packages=find_packages(),
    install_requires=['dict-recursive-update == 1.0.1']
)
