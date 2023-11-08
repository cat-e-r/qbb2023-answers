#!/usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 



def parse_bedgraphs(fname):
    data = set()
    coverages = []
    with open(fname, 'r') as file:
        for line in file:
            parts = line.strip().split()
            #chrom = int(parts[0])
            start = int(parts[1])
            #end = int(parts[2])
            methylation = float(parts[3])
            cov = int(parts[4])
            data.add(start)
            coverages.append(cov)
    return data, coverages, methylation

norm_ONT, norm_bisulfite_f, wildt_ONT, wildt_bi, tumor_ONT, tumor_bi= sys.argv[1:7]

norm, norm_cov, norm_meth = parse_bedgraphs(norm_ONT)
norm_bisulfite, norm_bi_cov, norm_bi_meth = parse_bedgraphs(norm_bisulfite_f)
wt_ONT, wt_cov_ONT, wt_meth_ONT = parse_bedgraphs(wildt_ONT)
wt_bi, wt_cov_bi, wt_meth_bi = parse_bedgraphs(wildt_bi)
tum_ONT, tum_cov_ONT, tum_meth_ONT = parse_bedgraphs(tumor_ONT)
tum_bi, tum_cov_bi, tum_meth_bi = parse_bedgraphs(tumor_bi)

norm_nano = set()
norm_bi = set()
norm_all = set()
for i in norm:
    if i not in norm_bisulfite:
        norm_nano.add(i)
    else:
        norm_all.add(i)
for i in norm_bisulfite:
    if i not in norm:
        norm_bi.add(i)

print(len(norm_nano)/(len(norm_nano)+len(norm_bi)+len(norm_all))*100)
print(len(norm_bi)/(len(norm_nano)+len(norm_bi)+len(norm_all))*100)
print(len(norm_all)/(len(norm_nano)+len(norm_bi)+len(norm_all))*100)

#plot
fig, ax = plt.subplots()

ax.hist(norm_nano)

ax.set_title( "Nanopore vs. Bisulfite Sequencing Coverage")
ax.hist(norm_cov, label = 'Nanopore', alpha = 0.6, color = 'mediumseagreen', bins = 320)
ax.hist(norm_bi_cov, label = 'Bisulfite', alpha = 0.5, color = 'deeppink', bins = 920)
ax.set_xlabel("Coverage")
ax.set_ylabel("Ocurrances")
ax.set_xlim(0,100)
ax.legend()
plt.tight_layout()
fig.savefig( "bisulfite_v_nano_cov.png" )

ONT_meth_scores = {}
with open("ONT.cpg.chr2.bedgraph", 'r') as file:
    for line in file:
        data = line.strip().split()
        start = int(data[1])
        meth = float(data[3])
        ONT_meth_scores[start] = meth 

bi_meth_scores = {}
with open("bisulfite.cpg.chr2.bedgraph", 'r') as file:
    for line in file:
        data = line.strip().split()
        start = int(data[1])
        meth = float(data[3])
        bi_meth_scores[start] = meth 


nano_l = []
bi_l = []
nano_bi_diffs = []
for i in norm_all:
    nano_l.append(ONT_meth_scores[i])
    bi_l.append(bi_meth_scores[i])
    if (ONT_meth_scores[i] - bi_meth_scores[i]) != 0:
        nano_bi_diffs.append((ONT_meth_scores[i] - bi_meth_scores[i]))

plt.close()


fig, ax = plt.subplots()
hist, x_edges, y_edges = np.histogram2d(nano_l, bi_l)
hist = np.log10(hist + 1)
pearson_r = np.corrcoef(nano_l, bi_l)[0, 1]
#print(pearson_r)
plt.imshow(hist, extent=[x_edges[0], x_edges[-1], y_edges[0], y_edges[-1]])
plt.colorbar(label = 'log10(count + 1)')
plt.xlabel("Nano score")
plt.ylabel("Bisulfite score")
plt.title(f"Pearson R: {pearson_r}")
plt.savefig('hist2d.png')

#violin
plt.close()

ONT_wt_set = set()
ONT_tum_set = set()
ONT_wt_tum = set()
for i in wt_ONT:
    if i not in tum_ONT:
        ONT_wt_set.add(i)
    else:
        ONT_wt_tum.add(i)
for i in tum_ONT:
        if i not in wt_ONT:
            ONT_tum_set.add(i)

bi_wt_set = set()
bi_tum_set = set()
bi_wt_tum = set()
for i in wt_bi:
    if i not in tum_bi:
        bi_wt_set.add(i)
    else:
        bi_wt_tum.add(i)
for i in tum_bi:
        if i not in wt_bi:
            bi_tum_set.add(i)

wt_meth_scores = {}
with open("normal.ONT.chr2.bedgraph", 'r') as file:
    for line in file:
        data = line.strip().split()
        start = int(data[1])
        meth = float(data[3])
        wt_meth_scores[start] = meth 

tum_meth_scores = {}
with open("tumor.ONT.chr2.bedgraph", 'r') as file:
    for line in file:
        data = line.strip().split()
        start = int(data[1])
        meth = float(data[3])
        tum_meth_scores[start] = meth 

wt_bi_meth_scores = {}
with open("normal.bisulfite.chr2.bedgraph", 'r') as file:
    for line in file:
        data = line.strip().split()
        start = int(data[1])
        meth = float(data[3])
        wt_bi_meth_scores[start] = meth 

tum_bi_meth_scores = {}
with open("tumor.bisulfite.chr2.bedgraph", 'r') as file:
    for line in file:
        data = line.strip().split()
        start = int(data[1])
        meth = float(data[3])
        tum_bi_meth_scores[start] = meth 

ONT_wt_tum_diffs = []
for i in ONT_wt_tum:
    if wt_meth_scores[i] != tum_meth_scores[i]:
        ONT_wt_tum_diffs.append((wt_meth_scores[i] - tum_meth_scores[i]))

bi_wt_tum_diffs = []
for i in bi_wt_tum:
    if wt_bi_meth_scores[i] != tum_bi_meth_scores[i]:
        bi_wt_tum_diffs.append((wt_bi_meth_scores[i] - tum_bi_meth_scores[i]))

bi_r = []
ont_r = []
for i in bi_wt_tum:
    if i in ONT_wt_tum:
        bi_r.append(wt_bi_meth_scores[i] - tum_bi_meth_scores[i])
        ont_r.append(wt_meth_scores[i] - tum_meth_scores[i])

fig, ax = plt.subplots()
plt.violinplot([ONT_wt_tum_diffs, bi_wt_tum_diffs])
ax.set_xticks([1,2], ['ONT: wt v tum', 'Bisulfite: wt v tum'])
pearson_r_violin = np.corrcoef(bi_r, ont_r)[0,1]
ax.set_title(f"Pearson R: {pearson_r_violin}")
plt.savefig("violin.png")








