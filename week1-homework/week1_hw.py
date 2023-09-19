#!/usr/bin/env python

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

import scipy.stats as sps
import statsmodels.formula.api as smf
import statsmodels.api as sm

# EXERCISE 1: Wrangle the data
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

# Step 1.3

my_dictionary_DF = pd.DataFrame.from_dict(my_dictionary, orient = 'index', columns = ['maternal_dnm', 'paternal_dnm'])

# Step 1.4

par_data = pd.read_csv('aau1043_parental_age.csv', index_col = 'Proband_id')

# Step 1.5

total_data = pd.concat([my_dictionary_DF, par_data], axis = 1, join = 'inner')

print(total_data)

#________________________________________________________________________________________________

# EXERCISE 2: Fit and interpret linear regression models with Python

# Step 2.1

x_f = total_data.loc[:, "Mother_age"]
y_f = total_data.loc[:, "maternal_dnm"]

fig, ax = plt.subplots()
ax.set_title( "Maternal de novo Mutations \n with Age")
ax.scatter(x_f, y_f, c = 'pink')
#ax.hist(x)
ax.set_xlabel("maternal age")
ax.set_ylabel("de novo mutations")
plt.tight_layout()
figure = fig.savefig( "ex2_a.png" )
#plt.show()

x_m = total_data.loc[:, "Father_age"]
y_m = total_data.loc[:, "paternal_dnm"]

fig, ax = plt.subplots()
ax.set_title( "Paternal de novo Mutations \n with Age")
ax.scatter(x_m, y_m, c = 'cyan')
#ax.hist(x)
ax.set_xlabel("paternal age")
ax.set_ylabel("de novo mutations")
plt.tight_layout()
figure = fig.savefig( "ex2_b.png" )
#plt.show()

# Step 2.2

mat_ols = smf.ols(formula = 'maternal_dnm ~ 1 + Mother_age' , data = total_data)
mat_ols_fit = mat_ols.fit()
print(mat_ols_fit.params)
print(mat_ols_fit.pvalues)
print(mat_ols_fit.summary())
#see README.md for analysis

# Step 2.3

pat_ols = smf.ols(formula = 'paternal_dnm ~ 1 + Father_age' , data = total_data)
pat_ols_fit = pat_ols.fit()
print(pat_ols_fit.summary())
#see README.md for analysis

# Step 2.4
#see README.md for answer

# Step 2.5

fig, ax = plt.subplots()
ax.set_title( "Paternal vs. Maternal\nde novo Mutations")
ax.hist(y_m, label = 'maternal', alpha = 0.5, color = 'pink')
ax.hist(y_f, label = 'paternal', alpha = 0.4, color = 'cyan')
ax.set_xlabel("# of de novo mutations")
ax.set_ylabel("ocurrances")
ax.legend()
plt.tight_layout()
figure = fig.savefig( "ex2_c.png" )
plt.show()

# Step 2.6
print(sps.ttest_ind(y_m, y_f))
#see analysis in README.md





