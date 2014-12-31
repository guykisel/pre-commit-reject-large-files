#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import argparse
import os


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='filenames to run')
    parser.add_argument('-m', '--max_filesize', type=int,
                        help='maximum allowable filesize in bytes',
                        default=5242880)
    args = parser.parse_args(argv)

    return_value = 0

    for filename in args.filenames:
        size = os.stat(filename).st_size
        if int(size) > int(args.max_filesize):
            print('{} is too large ({} > {})'.format(os.path.abspath(filename),
                                                     size, args.max_filesize))
            return_value = 1
    return return_value


if __name__ == '__main__':
    exit(main())
