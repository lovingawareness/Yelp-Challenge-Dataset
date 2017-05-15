#!/usr/bin/python
import json

def load_json(json_filename):
    data = list()
    with open(json_filename) as f:
        for line in f:
            data.append(json.loads(f))
    return data

data = load_json('yelp_academic_dataset_business.json')

for row in data:
    if row['attributes']:
        attributes = row['attributes']
        all_attributes += [attribute.split(':')[0] for attribute in attributes]

# De-dupe
all_attributes = list(set(all_attributes))

with open('yelp_academic_dataset_business-attributes.txt', 'w') as f:
    for attribute in sorted(all_attributes):
        f.write(attribute + '\n')

