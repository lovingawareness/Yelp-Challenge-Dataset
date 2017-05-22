#!/usr/bin/python
echo Performing additional transformations on yelp_academic_dataset_business.csv.
python process_business_restaurants.py
echo Performing additional transformations on yelp_academic_dataset_user.csv.
python process_user_elitegroup.py
echo Performing additional transformations on yelp_academic_dataset_review.csv.
python process_reviews_wordcount.py
