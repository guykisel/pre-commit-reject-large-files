#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import sys

from setuptools import find_packages, setup

install_requires = []
if sys.version_info < (2, 7):
    install_requires.append('argparse')

setup(
    name='pre_commit_reject_large_files',
    description='A pre-commit hook to reject large files.',
    url='https://github.com/guykisel/pre-commit-reject-large-files',
    version='0.0.1dev0',
    author='Guy Kisel',
    author_email='guy.kisel@gmail.com',
    platforms='any',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
    ],
    packages=find_packages('.', exclude=('tests*', 'testing*')),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            ('reject-large-files = '
             'pre_commit_reject_large_files.reject:main'),
        ],
    },
)
