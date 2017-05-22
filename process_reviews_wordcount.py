#!/usr/bin/python
from __future__ import print_function
from tqdm import tqdm
import unicodecsv as csv
from collections import defaultdict
import json

print("Processing yelp_academic_dataset_review.csv into yelp_academic_dataset_review-wordcount.csv...")
with open('yelp_academic_dataset_review.csv', 'rU') as f_in:
    dr = csv.DictReader(f_in, encoding='UTF8')
    fieldnames = dr.fieldnames
    fieldnames.remove('text')
    fieldnames.remove('stars')
    fieldnames.append('text_wordcount')
    fieldnames.append('review_stars')
    with open('yelp_academic_dataset_review-wordcount.csv', 'wb') as f_out:
       dw = csv.DictWriter(f_out, fieldnames=fieldnames, encoding='UTF8') 
       dw.writeheader()
       for row in tqdm(dr):
           # Basic wordcount - how many chunks after splitting by spaces
           if row['text']:
               row['text_wordcount'] = len(row['text'].split(' '))
               row['review_stars'] = row['stars']
               row.pop('text')
               row.pop('stars')
               dw.writerow(row)
print("Done!")
