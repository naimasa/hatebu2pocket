# -*- coding: utf-8 -*-
import sys
import pocket
from xml.etree.ElementTree import *
import json

param = sys.argv
if (len(param) < 2):
    print "invalid auguments"
    exit(1)

# parse xml
infile = param[1]
tree = parse(infile)
elem = tree.getroot()

list = []
for e in elem.findall(".//{http://purl.org/atom/ns#}link[@rel='related']"):
  url = e.get("href");
  list.append({'action' : 'add', 'url' : url})

# load to pocket (bulk add)
api = pocket.Api(consumer_key='57245-2a642b94f19c5d3e591bce26',
                 access_token='your_access_token')

actions = api.send(json.dumps(list));

# print results
for action in actions:
    if action["response_code"] != "200":
        print action["response_code"] + ":" + action["resolved_url"]
