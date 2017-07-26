#!/usr/local/bin/python

import unicodecsv as csv
import json
import sys


def load_dump(filename):
    leaky = []
    with open(filename) as f:
        for line in f.readlines():
            leaky.append(json.loads(line))
    return leaky


def make_node_and_relationship_lists(objects):
    nodes = [['address', 'type', 'size', 'name', 'value']]
    relationships = [['start', 'end']]


    for item in objects:
        row = [
            item['address'],
            item['type'],
            item['size'],
            item.get('name', '').replace("\"", "&quot;").replace(",", "&comma;"),
            unicode(item.get('value', '')).replace("\"", "&quot;").replace(",", "&comma;")
        ]
        nodes.append(row)

        for child in item['refs']:
            relationships.append([item['address'], child])

    return nodes, relationships


def write_to_csv(list_of_lists, name):
    with open(name, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(list_of_lists)


objs = load_dump(sys.argv[1])
nodes, relationships = make_node_and_relationship_lists(objs)
write_to_csv(nodes, "nodes-{}".format(sys.argv[1]))
write_to_csv(relationships, "rels-{}".format(sys.argv[1]))
