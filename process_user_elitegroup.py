#!/usr/bin/python
from __future__ import print_function
import unicodecsv as csv
from tqdm import tqdm


columns_to_keep = \
{"average_stars": "stars_user",                  \
 "compliment_cool": "compliment_cool",           \
 "compliment_cute": "compliment_cute",           \
 "compliment_funny": "compliment_funny",         \
 "compliment_hot": "compliment_hot",             \
 "compliment_list": "compliment_list",           \
 "compliment_more": "compliment_more",           \
 "compliment_note": "compliment_note",           \
 "compliment_photos": "compliment_photos",       \
 "compliment_plain": "compliment_plain",         \
 "compliment_profile": "compliment_profile",     \
 "compliment_writer": "compliment_writer",       \
 "cool": "cool",                                 \
 "fans": "fans",                                 \
 "friends": "friends",                           \
 "funny": "funny",                               \
 "review_count": "review_count_user",            \
 "useful": "useful",                             \
 "yelping_since": "yelping_since"};

print("Processing yelp_academic_dataset_user.csv into yelp_academic_dataset_user-elitegroup.csv...")
with open('yelp_academic_dataset_user.csv', 'rU') as f_in:
    dr = csv.DictReader(f_in, encoding='UTF8')
    with open('yelp_academic_dataset_user-elitegroup.csv', 'wb') as f_out:
        dw = csv.DictWriter(f_out, encoding='UTF8', fieldnames=sorted(columns_to_keep.values() + ['elitegroup']))
        dw.writeheader()
        for row in tqdm(dr):
            new_row = {}
            for original_key, new_key in columns_to_keep.iteritems():
                new_row[new_key] = row[original_key]
            # Calculation of the 'elitegroup' column
            # Default value of 2
            elitegroup = 2
            # Has this user been elite in the past 3 years? Then we set elitegroup to 1
            if row['elite_2016'] == 'True' and row['elite_2015'] == 'True' and row['elite_2014'] == 'True':
                elitegroup = 1
            else:
                # Has the user never been elite? Then we set elitegroup to 0
                if row['elite_None'] == 'True':
                    elitegroup = 0
            new_row['elitegroup'] = elitegroup
            dw.writerow(new_row)
print("Done!")
