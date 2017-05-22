#!/usr/bin/python
import unicodecsv as csv
from collections import defaultdict

with open('yelp_academic_dataset_review-wordcount.csv', 'rU') as f:
    reviews = list(csv.DictReader(f, encoding='utf8'))
with open('yelp_academic_dataset_business-restaurants.csv', 'rU') as f:
    businesses = list(csv.DictReader(f, encoding='utf8'))
with open('yelp_academic_dataset_user-elitegroup.csv', 'rU') as f:
    users = list(csv.DictReader(f, encoding='utf8'))

businesses_by_id = {b['business_id']: b for b in businesses}
users_by_id = {u['user_id']: u for u in users}

reviews_by_business_id = defaultdict(lambda: [])
for review in reviews:
    reviews_by_business_id[review['business_id']].append(review)

new_rows = []
for business_id, business in businesses_by_id.iteritems():
    for review in reviews_by_business_id.get(business_id, []):
        joined_row = {}
        joined_row.update(business)
        joined_row.update(review)
        joined_row.update(users_by_id[review['user_id']])
        new_rows.append(joined_row)


with open('business_review_users-merged.csv', 'wb') as f:
    dw = csv.DictWriter(f, encoding='utf8', fieldnames=sorted(new_rows[0].keys()))
    dw.writeheader()
    dw.writerows(new_rows)
