#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys


def wc_map(line):
    return [(key, 1) for key in re.split(r'\s', line.strip()) if key]


def output(records):
    for key, value in records:
        print '{0}\t{1}'.format(key, value)

for l in sys.stdin:
    output(wc_map(l))
