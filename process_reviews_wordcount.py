#!/usr/bin/python
from __future__ import print_function
from tqdm import tqdm
import unicodecsv as csv
import json

print("Processing yelp_academic_dataset_review.json into yelp_academic_dataset_review-wordcount.csv...")
output_rows = []
with open('yelp_academic_dataset_review.json', 'rb') as f_in:
    for line in tqdm(f_in):
        review = json.loads(line)
        text = review['text'] or ''
        review['text_wordcount'] = len(text.split(' '))
        review['stars_review'] = review['stars']
        review.pop('text')
        review.pop('stars')
        output_rows.append(review)

with open('yelp_academic_dataset_review-wordcount.csv', 'wb') as f_out:
    dw = csv.DictWriter(f_out, fieldnames=sorted(output_rows[0].keys()), encoding='utf8')
    dw.writeheader()
    dw.writerows(output_rows)
print("Done!")
