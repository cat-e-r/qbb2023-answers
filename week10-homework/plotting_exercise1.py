#!/usr/bin/env python

import numpy as np
import pandas as pd
from pydeseq2 import preprocessing
from matplotlib import pyplot as plt

# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

# normalize
counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

# log
counts_df_logged = np.log2(counts_df_normed + 1)

# merge with metadata
full_design_df = pd.concat([counts_df_logged, metadata], axis=1)

# do I need to run a regression for all the genes like last week?

# Step 1.1: Distribution of gene expression level for subject GTEX-113JC
# get all expression levels from GTEX-113JC (exclude last 3 columns)
data_11 = full_design_df.loc['GTEX-113JC',:'MT-TP']
data_11 = data_11[data_11 != 0]
# make histogram
fig, ax = plt.subplots()
ax.set_title( "Expression levels for GTEX-113JC")
ax.hist(data_11, bins = 25, color = 'pink')
ax.set_xlabel("Expression level")
ax.set_ylabel("Ocurrances")
plt.tight_layout()
figure = fig.savefig( "Step1_1.png" )

# Step 1.2: Distribution of expression level across all subjects for gene MXD4 in Males v Females
# get expression levels for females vs males from MXD4 column
data_12 = full_design_df.loc[:,['MXD4', 'SEX']]

mxd4_m = data_12[data_12['SEX'] == 1]
mxd4_f = data_12[data_12['SEX'] == 2]

# make histogram with diff colors and legend
fig, ax = plt.subplots()
ax.set_title( "Female vs. Male\nMXD4 expression")
ax.hist(mxd4_m['MXD4'], label = 'male', bins = 25, alpha = 0.4, color = 'cyan')
ax.hist(mxd4_f['MXD4'], label = 'female',bins = 15, alpha = 0.5, color = 'pink')
ax.set_xlabel("Expression level")
ax.set_ylabel("Ocurrances")
ax.legend()
plt.tight_layout()
figure = fig.savefig( "Step1_2.png" )


#print(full_design_df)
# # Step 1.3: Distribution of subject ages
data_13 = full_design_df['AGE'].value_counts()
sortOrder = ["20-29", "30-39", "40-49", "50-59", "60-69", "70-79"]
data_13 = data_13.loc[sortOrder]


# make histogram
fig, ax = plt.subplots()
ax.set_title( "Subject Age Distribution")
ax.bar(data_13.index, data_13, color = 'pink')
ax.set_xlabel("Ages")
ax.set_ylabel("Ocurrances")
plt.tight_layout()
figure = fig.savefig( "Step1_3.png" )

# Step 1.4: male v female median expression of LPXN as it changes with age
# split into male and female
data_14 = full_design_df.loc[:,['LPXN', 'SEX', 'AGE']]
LPXN_m = data_14[data_14['SEX'] == 1]
LPXN_f = data_14[data_14['SEX'] == 2]

ages = ["20-29", "30-39", "40-49", "50-59", "60-69", "70-79"]
med_exp_m = []
med_exp_f = []
for age in ages:
    # Subset your LPXN_m and LPXN_f to just this age
    age_spec_m = LPXN_m[LPXN_m['AGE'] == age]
    age_spec_f = LPXN_f[LPXN_f['AGE'] == age]
    med_m = np.median(age_spec_m['LPXN'])
    med_f = np.median(age_spec_f['LPXN'])
    med_exp_m.append(med_m)
    med_exp_f.append(med_f)

# make line plot w/ age as x axis, expression level as y axis, for males vs females
fig, ax = plt.subplots()
ax.set_title( "Male vs Female Median LPXN Expression\nOver Time")
ax.plot(ages, med_exp_m, label = 'male', color = 'dodgerblue')
ax.plot(ages, med_exp_f, label = 'female', color = 'hotpink')
ax.set_xlabel("Age")
ax.set_ylabel("Median LPXN Expression Level")
ax.legend()
plt.tight_layout()
figure = fig.savefig( "Step1_4.png" )











