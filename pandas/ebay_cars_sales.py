# -*- coding: utf-8 -*-
"""ebay_cars_sales.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VnvNt3L7Zy5kXu-VH60-YumPr57pxfno

In this project, we'll work with a dataset of used cars from eBay Kleinanzeigen, a classifieds section of the German eBay website. The dataset contains over 370000 used cars. The aim of this project is to clean and analyze the included cars listings.
The dataset can be downloaded: Here
The data dictionary provided with data is as follows:

dateCrawled - When this ad was first crawled. All field-values are taken from this date.
name - Name of the car.
seller - Whether the seller is private or a dealer.
offerType - The type of listing
price - The price on the ad to sell the car.
abtest - Whether the listing is included in an A/B test.
vehicleType - The vehicle Type.
yearOfRegistration - The year in which the car was first registered.
gearbox - The transmission type.
powerPS - The power of the car in PS.
model - The car model name.
kilometer - How many kilometers the car has driven.
monthOfRegistration - The month in which the car was first registered.
fuelType - What type of fuel the car uses.
brand - The brand of the car.
notRepairedDamage - If the car has a damage which is not yet repaired.
dateCreated - The date on which the eBay listing was created.
nrOfPictures - The number of pictures in the ad.
postalCode - The postal code for the location of the vehicle.
lastSeenOnline - When the crawler saw this ad last online.
"""

import pandas as pd
import numpy as np

autos = pd.read_csv("/content/autos.csv",encoding="latin1")
autos.head()

autos.info()

autos.columns

autos.rename({'yearOfRegistration':'registration_year','gearbox':'gear_box','monthOfRegistration':'registration_month','notRepairedDamage':'unrepaired_damage','dateCreated':'ad_created','fuelType':'fuel_type','lastSeen':'last_seen','vehicleType':'vehicle_type','dateCrawled':'date_crawled','offerType':'offer_type','abtest':'ab_test','nrOfPictures':'num_of_pics','postalCode':'postal_code','powerPS':'power_ps'},axis=1, inplace=True)

autos.columns

autos.describe()

autos['price'].value_counts(normalize=True).sort_index(ascending=False).head(20)

autos=autos[autos['price'].between(1,350000)]

autos.describe()

autos['kilometer'].value_counts(normalize=True).sort_index(ascending=False).head(20)

autos[['date_crawled','ad_created','last_seen']][0:5]

autos['date_crawled'].str[:10]

autos['date_crawled'].str[:10].value_counts(normalize=True,dropna=True).sort_index(ascending=False)

autos.groupby('brand')['price'].mean().plot(kind='bar')

autos['gear_box'].value_counts()

