#!/bin/bash
echo Converting all JSON files to CSV.
python convert.py
echo Re-converting yelp_academic_dataset_business.json to CSV in the way we want.
python process_business.py
echo Re-converting yelp_academic_dataset_user.json to CSV in the way we want.
python process_user.py
echo Creating samples of CSV files.
sh make_samples.sh
echo Zipping the new CSV files.
zip yelp_academic_dataset-CSV.zip yelp_academic_dataset_*.csv
