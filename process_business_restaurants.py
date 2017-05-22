#!/usr/bin/python
from __future__ import print_function
import unicodecsv as csv
from tqdm import tqdm

columns_to_keep = \
{"attribute_Ambience_casual": "attribute_Ambience_casual",                  \
 "attribute_Ambience_classy": "attribute_Ambience_classy",                  \
 "attribute_Ambience_divey": "attribute_Ambience_divey",                    \
 "attribute_Ambience_hipster": "attribute_Ambience_hipster",                \
 "attribute_Ambience_intimate": "attribute_Ambience_intimate",              \
 "attribute_Ambience_romantic": "attribute_Ambience_romantic",              \
 "attribute_Ambience_touristy": "attribute_Ambience_touristy",              \
 "attribute_Ambience_trendy": "attribute_Ambience_trendy",                  \
 "attribute_Ambience_upscale": "attribute_Ambience_upscale",                \
 "attribute_RestaurantsPriceRange2": "attribute_RestaurantsPriceRange2",    \
 "business_id": "business_id",                                              \
 "review_count": "review_count",                                            \
 "stars": "stars",                                                          \
 "categories": "categories",                                                \
 "city": "city"}

print("Processing yelp_academic_dataset_business.csv into yelp_academic_dataset_business-restaurants.csv...")
with open('yelp_academic_dataset_business.csv', 'rU') as f_in:
    dr = csv.DictReader(f_in, encoding='UTF8')
    fieldnames = dr.fieldnames
    with open('yelp_academic_dataset_business-restaurants.csv', 'wb') as f_out:
        dw = csv.DictWriter(f_out, encoding='UTF8', fieldnames=sorted(columns_to_keep.values()))
        dw.writeheader()
        for row in tqdm(dr):
            if 'Restaurant' in row['categories']:
                new_row = {}
                for original_key, new_key in columns_to_keep.iteritems():
                    new_row[new_key] = row[original_key]
                dw.writerow(new_row)
print("Done!")
