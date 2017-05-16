#!/usr/bin/python
from __future__ import print_function
import unicodecsv as csv
from tqdm import tqdm
import json

print("Reading data from JSON...")
data = list()
with open('yelp_academic_dataset_business.json') as f:
    for line in f:
        data.append(json.loads(line))


print("Calculating all categories represented in the data...")
all_categories = []
for row in data:
    if row['categories']:
        all_categories += row['categories']
all_categories = set(all_categories)

print("Calculating all attributes represented in the data...")
all_attributes = []
for row in data:
    if row['attributes']:
        for attribute_string in row['attributes']:
            all_attributes.append(attribute_string.split(':')[0])
all_attributes = set(all_attributes)

print("Writing attributes to file...")
with open('yelp_academic_dataset_business-attributes.txt', 'w') as f:
    f.write('\n'.join(sorted(list(all_attributes))))

print("Writing categories to file...")
with open('yelp_academic_dataset_business-categories.txt', 'w') as f:
    f.write('\n'.join(sorted(list(all_categories))))

print("Processing data...")
new_data = list()
for row in tqdm(data):
    new_row = {}
    for k, v in row.iteritems():
        if k not in ['hours', 'categories', 'attributes']:
            new_row[k] = v
        else:
            if k == 'hours' and row['hours']:
                for hour in row['hours']:
                    day, time_string = hour.split(' ')
                    new_row['hours_' + day] = time_string
            elif k == 'attributes' and row['attributes']:
                attributes = dict()
                for attribute_string in row['attributes']:
                    attribute = attribute_string.split(':')[0]
                    value = ':'.join(attribute_string.split(':')[1:])
                    attributes[attribute] = value
                for attribute in all_attributes:
                    new_row['attribute_' + attribute] = attributes.get(attribute, False)
            elif k == 'categories' and row['categories']:
                new_row['categories'] = ', '.join(sorted(row['categories']))
#                for category in all_categories:
#                    new_row['category_' + category] = (category in row['categories'])
    new_data.append(new_row)

print("Writing data to CSV file...")
with open('yelp_academic_dataset_business.csv', 'wb') as f:
    fieldnames = sorted(new_data[0].keys())
    dw = csv.DictWriter(f, fieldnames=fieldnames, encoding='UTF-8')
    dw.writeheader()
    dw.writerows(new_data)
