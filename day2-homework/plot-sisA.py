#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Get dataset to recreate Fig 3B from Lott et al 2011 PLoS Biology https://pubmed.gov/21346796
# wget https://github.com/bxlab/cmdb-quantbio/raw/main/assignments/lab/bulk_RNA-seq/extra_data/all_annotated.csv

f = open("all_annotated.csv", "r")
transcripts = f.readlines()

index = 0 #start a variable to iterate throgh and modify the items WITHIN the existing list

transcript_names = []

data_vals = []
for transcript in transcripts[1:]:
    transcript = transcript.rstrip() #gets rid of \n at the end of the patient string and stores it as the new patient
    transcript = transcript.split(",") #splits the string at the commas and stores it as the new patient
    transcript_names.append(transcript[0])
    #sample_names.append(transcript[1])
   # print(transcripts)

#print(transcript_names)
#print(transcript_names[0])
#print(transcript_names[1])

sample_names = []
samples = transcripts[0]
#print(samples)
samples = samples.rstrip() #gets rid of \n at the end of the patient string and stores it as the new patient
samples = samples.split(",")

for sample in samples[2:]:
    sample_names.append(sample)
print(sample_names)



#transcripts = np.loadtxt( "all_annotated.csv", delimiter=",", usecols=0, dtype="<U30", skiprows=1 )
#print( "transcripts: ", transcripts[0:5] )

samples = np.loadtxt( "all_annotated.csv", delimiter=",", max_rows=1, dtype="<U30" )[2:]
print( "samples: ", samples[0:5] )

data = np.loadtxt( "all_annotated.csv", delimiter=",", dtype=np.float32, skiprows=1, usecols=range(2, len(samples) + 2) )
print( "data: ", data[0:5, 0:5] )

# Find row with transcript of interest
for i in range(len(transcript_names)):
    if transcript_names[i] == 'FBtr0073461':
        row = i

# Find columns with samples of interest
f_cols = []
m_cols = []
for i in range(len(samples)):
    if "female" in samples[i]:
        f_cols.append(i)
    elif "male" in samples[i]:
        m_cols.append(i)

# Subset data of interest
f_expression = data[row, f_cols]
m_expression = data[row, m_cols]

# Prepare data
#x = samples[f_cols]
y_f = f_expression
y_m = m_expression
y_2m = 2 * np.array(m_expression)

x = ['10', '11', '12', '14', '14A', '14B', '14C', '14D']

# Plot data
fig, ax = plt.subplots()
ax.set_title( "sisA" )
ax.plot(x, y_f, c = "red")
ax.plot(x, y_m, c = "blue")
ax.plot(x, y_2m, c = "cyan")
ax.set_xlabel("Developmental Stage")
ax.set_ylabel("mRNA Abundance (RPKM)")
fig.savefig( "FBtr0073461.png" )
plt.tight_layout()
plt.show()
plt.close( fig )