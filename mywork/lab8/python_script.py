#!/bin/env python

import json

with open('/workspace/json-practice-mqq9sb/data/schacon.repos.json', 'r') as file:
    data = json.load(file)

new_file = []

for r in data[0:5]:
    name = r['name']
    html = r['html_url']
    update = r['updated_at']
    visibility = r['visibility']
    line = name+','+html+','+update+','+visibility
    new_file.append(line)

with open('/workspace/json-practice-mqq9sb/mywork/lab8/chacon.csv', 'w') as file:
    file.write('\n'.join(new_file))
