#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import pkg_resources

__version__ = pkg_resources.get_distribution(
    "pre_commit_reject_large_files").version
