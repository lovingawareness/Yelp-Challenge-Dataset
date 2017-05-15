#!/usr/bin/python
import json

data = list()
with open('yelp_academic_dataset_business.json') as f:
    for line in f:
        data.append(json.loads(f))

for row in data:
    if row['attributes']:
        attributes = row['attributes']
        all_attributes += [attribute.split(':')[0] for attribute in attributes]

# De-dupe
all_attributes = list(set(all_attributes))

with open('attributes.txt', 'w') as f:
    for attribute in sorted(all_attributes):
        f.write(attribute + '\n')
        
