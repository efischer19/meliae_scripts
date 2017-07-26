#!/usr/bin/python

import sys
import json

my_strings1 = {}
with open(sys.argv[1]) as fp:
    for line in fp:
        parsed = json.loads(line)
        if parsed['type'] == 'str' or parsed['type'] == 'unicode':
            my_strings1[parsed['address']] = parsed['value']


my_strings2 = {}
with open(sys.argv[2]) as fp:
    for line in fp:
        parsed = json.loads(line)
        if parsed['type'] == 'str' or parsed['type'] == 'unicode':
            my_strings2[parsed['address']] = parsed['value']

common_strings = set(my_strings1.values()).intersection(set(my_strings2.values()))

for k in sorted(my_strings1):
    if my_strings1[k] not in common_strings:
        print "{}:\t{}".format(k, my_strings1[k].encode('utf-8'))
