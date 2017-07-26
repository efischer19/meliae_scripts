#!/usr/bin/python

import sys
import json
from collections import defaultdict

total = [0, 0]
with open(sys.argv[1]) as fp:
    for line in fp:
        parsed = json.loads(line)
        total[0] += parsed['size']

with open(sys.argv[2]) as fp:
    for line in fp:
        parsed = json.loads(line)
        total[1] += parsed['size']

print "{} had {} more than {}, in total.".format(sys.argv[1], total[0]-total[1], sys.argv[2])
