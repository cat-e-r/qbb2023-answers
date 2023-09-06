#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Get dataset to recreate Fig 3B from Lott et al 2011 PLoS Biology https://pubmed.gov/21346796
# wget https://github.com/bxlab/cmdb-quantbio/raw/main/assignments/lab/bulk_RNA-seq/extra_data/all_annotated.csv

transcripts = np.loadtxt( "all_annotated.csv", delimiter=",", usecols=0, dtype="<U30", skiprows=1 )
print( "transcripts: ", transcripts[0:5] )

samples = np.loadtxt( "all_annotated.csv", delimiter=",", max_rows=1, dtype="<U30" )[2:]
print( "samples: ", samples[0:5] )

data = np.loadtxt( "all_annotated.csv", delimiter=",", dtype=np.float32, skiprows=1, usecols=range(2, len(samples) + 2) )
print( "data: ", data[0:5, 0:5] )

# Find row with transcript of interest
for i in range(len(transcripts)):
    if transcripts[i] == 'FBtr0073461':
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
x = samples[f_cols]
y_f = f_expression
y_m = m_expression
y_2m = 2 * np.array(m_expression)

# Plot data
fig, ax = plt.subplots()
ax.set_title( "FBtr0073461" )
ax.plot( x, y_f )
ax.plot(x, y_m)
ax.plot(x, y_2m)
ax.set_xlabel("Sample Number")
ax.set_ylabel("mRNA Abundance (RPKM)")
fig.savefig( "FBtr0073461.png" )
plt.close( fig )