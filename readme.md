<img src="http://imgur.com/KYfB2Ly.jpg?1" width="200" alt="Northwestern University | Kellogg School of Management" />

# Introduction

An update of [Yelp-Challenge-Dataset](https://github.com/vc1492a/Yelp-Challenge-Dataset) for the 2017 dataset.

The dataset for 2017 is available from Yelp here: https://www.yelp.com/dataset_challenge/

This will process the JSON files for the businesses and reviews, but does not treat the photo data. This reformats the JSON files into CSV files.

This was motivated by a request made by a team of MBA students at the [Kellogg School of Management](https://www.kellogg.northwestern.edu/) at [Northwestern University](https://www.northwestern.edu/), who wanted to use the data for an in-class project but wanted to analyze the data in Stata.

# How to run it

Clone this repository to your computer with `git clone https://github.com/tothebeat/Yelp-Challenge-Dataset.git` and change directory into it.

Download the business data dump from Yelp and extract directly into this folder.

This depends on some Python scripts, written with Python 2. You can create a Python virtual environment and install the required libraries with `pip install -r requirements.txt`.

Run `./process_all.sh`.

You should then find the following files:

* yelp_academic_dataset_business.csv
* yelp_academic_dataset_user.csv
* yelp_academic_dataset_checkin.csv
* yelp_academic_dataset_tip.csv
* yelp_academic_dataset_review.csv
* yelp_academic_dataset-CSV.zip
* data_samples/yelp_academic_dataset_business-head1000.csv
* data_samples/yelp_academic_dataset_user-head1000.csv
* data_samples/yelp_academic_dataset_checkin-head1000.csv
* data_samples/yelp_academic_dataset_tip-head1000.csv
* data_samples/yelp_academic_dataset_review-head1000.csv
* yelp_academic_dataset-CSV-samples.zip
* yelp_academic_dataset_business-attributes.txt
* yelp_academic_dataset_business-categories.txt

# What it does

It builds off of [this gist](https://gist.github.com/paulgb/5265767/) to convert the nested dictionary structure of the JSON files into a CSV. For our purposes, this is okay for the files yelp_academic_dataset_tip.json, yelp_academic_dataset_review.json, and yelp_academic_dataset_checkin.json, but there are more complex data types in yelp_academic_dataset_user.json and yelp_academic_dataset_business.json.

There are custom scripts to handle each of yelp_academic_dataset_business.json and yelp_academic_dataset_user.json, and below I describe that special handling.

## yelp_academic_dataset_business.json

In the business dataset, there are three keys on each record with specially formatted values: hours, attributes, and categories.

### hours

Here's an example of the value for the 'hours' key for the first data record in the file:

```
["Monday 11:0-21:0","Tuesday 11:0-21:0","Wednesday 11:0-21:0","Thursday 11:0-21:0","Friday 11:0-22:0"
,"Saturday 10:0-22:0","Sunday 11:0-18:0"]
```

This is translated to the CSV file as individual columns representing each day, and the value is the time range. The above will appear in the resulting CSV as:

```
hours_Friday,hours_Monday,hours_Saturday,hours_Sunday,hours_Thursday,hours_Tuesday,hours_Wednesday
11:0-22:0,11:0-21:0,10:0-22:0,11:0-18:0,11:0-21:0,11:0-21:0,11:0-21:0
```

### attributes

Here's an example of the value for the 'attributes' key for the first data record in the file:

```
["BikeParking: True","BusinessAcceptsBitcoin: False","BusinessAcceptsCreditCards: True","BusinessParking: {'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}","DogsAllowed: F
alse","RestaurantsPriceRange2: 2","WheelchairAccessible: True"]
```

Since most of these are boolean values, except for the more complicated 'BusinessParking' attribute, we're mostly interested in representing True or some value as True, and False or the lack of the attribute as False.

For attributes like 'BusinessParking' that clearly have sub-attributes, these sub-attribute strings are parsed as Python code, unpacked as dictionaries, and each sub-attribute results in a new column as well.

Each record in the resulting CSV has a column for every attribute represented in the file, prefixed by 'attribute\_', and the value for that column is True if the attribute is present and its value is True or present, and False if the attribute is not present or it is but its value is False.

The above data would be represented as follows:

```
attribute_AcceptsInsurance,attribute_AgesAllowed,attribute_Alcohol,attribute_Ambience_casual,attribute_Ambience_classy,attribute_Ambience_divey,attribute_Ambience_hipster,attribute_Ambience_intimate,attribute_Ambience_romantic,attribute_Ambience_touristy,attribute_Ambience_trendy,attribute_Ambience_upscale,attribute_BYOB,attribute_BYOBCorkage,attribute_BestNights_friday,attribute_BestNights_monday,attribute_BestNights_saturday,attribute_BestNights_sunday,attribute_BestNights_thursday,attribute_BestNights_tuesday,attribute_BestNights_wednesday,attribute_BikeParking,attribute_BusinessAcceptsBitcoin,attribute_BusinessAcceptsCreditCards,attribute_BusinessParking_garage,attribute_BusinessParking_lot,attribute_BusinessParking_street,attribute_BusinessParking_valet,attribute_BusinessParking_validated,attribute_ByAppointmentOnly,attribute_Caters,attribute_CoatCheck,attribute_Corkage,attribute_DietaryRestrictions_dairy-free,attribute_DietaryRestrictions_gluten-free,attribute_DietaryRestrictions_halal,attribute_DietaryRestrictions_kosher,attribute_DietaryRestrictions_soy-free,attribute_DietaryRestrictions_vegan,attribute_DietaryRestrictions_vegetarian,attribute_DogsAllowed,attribute_DriveThru,attribute_GoodForDancing,attribute_GoodForKids,attribute_GoodForMeal_breakfast,attribute_GoodForMeal_brunch,attribute_GoodForMeal_dessert,attribute_GoodForMeal_dinner,attribute_GoodForMeal_latenight,attribute_GoodForMeal_lunch,attribute_HairSpecializesIn_africanamerican,attribute_HairSpecializesIn_asian,attribute_HairSpecializesIn_coloring,attribute_HairSpecializesIn_curly,attribute_HairSpecializesIn_extensions,attribute_HairSpecializesIn_kids,attribute_HairSpecializesIn_perms,attribute_HairSpecializesIn_straightperms,attribute_HappyHour,attribute_HasTV,attribute_Music_background_music,attribute_Music_dj,attribute_Music_jukebox,attribute_Music_karaoke,attribute_Music_live,attribute_Music_no_music,attribute_Music_video,attribute_NoiseLevel,attribute_Open24Hours,attribute_OutdoorSeating,attribute_RestaurantsAttire,attribute_RestaurantsCounterService,attribute_RestaurantsDelivery,attribute_RestaurantsGoodForGroups,attribute_RestaurantsPriceRange2,attribute_RestaurantsReservations,attribute_RestaurantsTableService,attribute_RestaurantsTakeOut,attribute_Smoking,attribute_WheelchairAccessible,attribute_WiFi
False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,True,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,2,False,False,False,False,True,False
```

### categories

Here's an example of the value for the 'categories' key for the first data record in the file:

```
["Tobacco Shops","Nightlife","Vape Shops","Shopping"]
```

In the CSV file, this appears as a single column called 'categories' with the above values joined by ', '. So the above would become:

```
"Nightlife, Shopping, Tobacco Shops, Vape Shops"
```

Whatever the original ordering of the categories, it will output in alphabetical order.

## yelp_academic_dataset_user.json

In the user dataset, there are two keys on each record with specially formatted values, 'elite' and 'friends'.

### elite

Here's an example of the value for the 'elite' key for the first data record in the file:

```
["2017","2015","2016","2014","2011","2013","2012"]
```

This is a list of years during which the user was considered a Yelp Elite user.

In the resulting CSV, I collect all 'elite' years represented throughout the JSON file, create columns for each year prefixed by 'elite\_', and the value for that column is True or False depending on whether the user had elite status that year.

For this first user, their output data looks like:

```
elite_2005,elite_2006,elite_2007,elite_2008,elite_2009,elite_2010,elite_2011,elite_2012,elite_2013,elite_2014,elite_2015,elite_2016,elite_2017,elite_None
False,False,False,False,False,False,True,True,True,True,True,True,True,False
```

### friends

Here's an example of the value for the 'friends' key for the first data record in the file:

```
["iJg9ekPzF9lkMuvjKYX6uA","ctWAuzS04Xu0lke2Rop4lQ","B8CqppjOne8X4RSJ5KYOvQ","_K9sKlA4fVkWI4hyGSpoPA", ...]
```

This is abbreviated because it's a listing of all this user's friends' unique identifiers. This user in particular has 2313 such friends.

In the output, we don't care so much who the friends are but how many. In the CSV file, there will be a column called 'friends' with the value 2313.

## Post-processing

After these CSVs are created, sample CSVs are created in the data_samples subfolder with the first 1000 rows of each CSV. These are then zipped.

The large CSVs are also zipped for easy distribution.

## Who made this?

Nick Bennett [nicholas.bennett@kellogg.northwestern.edu](mailto:nicholas.bennett@kellogg.northwestern.edu), Senior Technical Support Specialist in [Kellogg Information Systems](https://kis.kellogg.northwestern.edu) at the [Kellogg School of Management](https://www.kellogg.northwestern.edu/).

If you want to learn how to do this on your own with your own data, I highly recommend the lessons at [DataCamp](https://www.datacamp.com/). It's a paid service, but I think extremely effective and worth it. See if you can get your employer to pay for it, as it may be directly beneficial if you're analyzing for work.
