#!/usr/bin/env python

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#Read in the data
cat_ref_df = pd.read_csv("cats_uk_reference.csv", index_col = 0)
squirrel_df = pd.read_csv("nyc_squirrels.csv")


#print(squirrel_df)

# diet = cat_ref_df.loc[:,['food_dry', 'food_wet', 'age_years']]

# wfood = diet[diet['food_dry'] == "False"]
# #wfood = wfood[wfood['food_wet'] == 'True']
# #dfood = diet[diet['food_wet'] == 'False']
# #dfood = dfood[dfood['food_dry'] == 'True']

# print(wfood)

#bar plot of main colors
main_color = squirrel_df['primary_fur_color'].value_counts()
order = ["Gray", "Cinnamon", "Black"]
sorted_main_color = main_color.loc[order]


fig, ax = plt.subplots()
ax.set_title( "Squirrel Color Distribution")
ax.bar(sorted_main_color.index, sorted_main_color, color = 'burlywood')
ax.set_xlabel("Squirrel Color")
ax.set_ylabel("Sightings")
plt.tight_layout()
figure = fig.savefig( "squirrel_plot_1.png" )

#scatter plot of long and lat
longitudes = squirrel_df['long']
lattitudes = squirrel_df['lat']

fig, ax = plt.subplots()
ax.set_title( "Squirrel Sightings Longitude and Latitude")
ax.scatter(longitudes, lattitudes, color = 'deepskyblue')
ax.set_xlabel("Longitude")
ax.set_ylabel("Lattitude")
plt.tight_layout()
figure = fig.savefig( "squirrel_plot_2.png" )

#dist of activities
nChasing = squirrel_df['chasing'].value_counts()[True]
nForaging = squirrel_df['foraging'].value_counts()[True]
nEating = squirrel_df['eating'].value_counts()[True]

activity_name = ["Chasing", "Foraging", "Eating"]
activity_counts = [nChasing, nForaging, nEating]


fig, ax = plt.subplots()
ax.set_title( "Squirrel Activity Distribution")
ax.bar(activity_name, activity_counts, color = 'mediumaquamarine')
ax.set_xlabel("Squirrel Activity")
ax.set_ylabel("Sightings")
plt.tight_layout()
figure = fig.savefig( "squirrel_plot_3.png" )



