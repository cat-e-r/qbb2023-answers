#!/usr/bin/env python

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

import scipy.stats as sps
import statsmodels.formula.api as smf
import statsmodels.api as sm

# Exercise 1: Wrangle the data
# Step 1.1

# You’ll start by exploring the data in aau1043_dnm.csv. First, load this data into a pandas dataframe.

df = pd.read_csv('aau1043_dnm.csv')
#print(df)

# Step 1.2

# You first want to count the number of paternally and maternally 
#inherited DNMs in each proband. Using this dataframe, create a 
#dictionary where the keys are the proband IDs and the value 
#associated with each key is a list of length 2, where the first 
#element in the list is the number of maternally inherited DNMs 
#and the second element in the list is the number of paternally 
#inherited DNMs for that proband. You can ignore DNMs without 
#a specified parent of origin.


pat_dnms = df.loc[:,"Phase_combined"] == "father"
pat_pro_id = df.loc[pat_dnms, "Proband_id"]
mat_dnms = df.loc[:,"Phase_combined"] == "mother"
mat_pro_id = df.loc[mat_dnms, "Proband_id"]

#print (pat_pro_id)
#print(mat_pro_id)

my_dictionary = {}
for i in df.loc[:, "Proband_id"]:
    my_dictionary[i] = [0, 0]

for pbid in mat_pro_id:
    my_dictionary[pbid][0] += 1

for pbid in pat_pro_id:
    my_dictionary[pbid][1] += 1


#print(my_dictionary)

my_dictionary_DF = pd.DataFrame.from_dict(my_dictionary, orient = 'index', columns = ['maternal_dnm', 'paternal_dnm'])

par_data = pd.read_csv('aau1043_parental_age.csv', index_col = 'Proband_id')

total_data = pd.concat([my_dictionary_DF, par_data], axis = 1, join = 'inner')

print(total_data)













