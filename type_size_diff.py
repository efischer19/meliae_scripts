#!/usr/bin/python

import sys
from collections import defaultdict

my_dict = defaultdict(int)
with open(sys.argv[1]) as fp:
    for line in fp:
        values = line.split(":")
        my_dict[values[0]] += int(values[1])

my_dict2 = defaultdict(int)
with open(sys.argv[2]) as fp:
    for line in fp:
        values = line.split(":")
        my_dict2[values[0]] += int(values[1])

my_dict3 = {}
for key in my_dict:
    val1 = my_dict[key]
    val2 = my_dict2.get(key, 0)
    my_dict3[key] = val1-val2

for w in sorted(my_dict3, key=my_dict3.get, reverse=True):
    print "{}, {} to {}, diff: -{}, {}%".format(w, my_dict[w], my_dict2.get(w, 0), my_dict3[w], my_dict3[w]*100.0/my_dict[w])
