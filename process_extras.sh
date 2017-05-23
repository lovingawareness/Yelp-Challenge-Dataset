#!/bin/bash
echo Performing additional transformations on yelp_academic_dataset_business.csv.
python process_business_restaurants.py
echo Performing additional transformations on yelp_academic_dataset_user.csv.
python process_user_elitegroup.py
echo Performing additional transformations on yelp_academic_dataset_review.csv.
python process_reviews_wordcount.py
echo Merging business, user, and review files on business_id and user_id.
python merge_business_review_user.py
