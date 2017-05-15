#!/usr/bin/python
import json

data = list()
with open('yelp_academic_dataset_business.json') as f:
    for line in f:
        data.append(json.loads(line))


