#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

results = {}


def wc_reduce(line):
    key, value = re.split(r'\t', line.strip())
    if not key in results:
        results[key] = 0
    results[key] = results[key] + int(value)


def output(records):
    for k, v in records:
        print '{0}\t{1}'.format(k, v)

for l in sys.stdin:
    wc_reduce(l)
output(sorted(results.items()))
