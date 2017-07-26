#!/usr/bin/python

import sys
import json
from collections import defaultdict

my_types = defaultdict(int)
type_instance_count = defaultdict(int)
with open(sys.argv[1]) as fp:
    for line in fp:
        parsed = json.loads(line)
        my_types[parsed['type']] += parsed['size']
        type_instance_count[parsed['type']] += 1

for w in sorted(my_types, key=my_types.get, reverse=True):
    print "{}:{}:{}".format(w, my_types[w], type_instance_count[w])
