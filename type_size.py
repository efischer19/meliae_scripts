#!/usr/bin/python

import sys
import json
from collections import defaultdict

my_types = defaultdict(int)
with open(sys.argv[1]) as fp:
    for line in fp:
        parsed = json.loads(line)
        my_types[parsed['type']] += parsed['size']

for w in sorted(my_types, key=my_types.get, reverse=True):
    print "{}:{}".format(w, my_types[w])
