#!/bin/bash
head -n 1000 yelp_academic_dataset_business.csv > ./data_samples/yelp_academic_dataset_business-head1000.csv
head -n 1000 yelp_academic_dataset_checkin.csv > ./data_samples/yelp_academic_dataset_checkin-head1000.csv
head -n 1000 yelp_academic_dataset_review.csv > ./data_samples/yelp_academic_dataset_review-head1000.csv
head -n 1000 yelp_academic_dataset_tip.csv > ./data_samples/yelp_academic_dataset_tip-head1000.csv
head -n 1000 yelp_academic_dataset_user.csv > ./data_samples/yelp_academic_dataset_user-head1000.csv
head -n 1000 yelp_academic_dataset_business-restaurants.csv > ./data_samples/yelp_academic_dataset_business-restaurants-head1000.csv
head -n 1000 yelp_academic_dataset_user-elitegroup.csv > ./data_samples/yelp_academic_dataset_user-elitegroup-head1000.csv
zip yelp_academic_dataset-CSV-samples.zip ./data_samples/*.csv
