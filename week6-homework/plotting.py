#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

PCs = np.loadtxt("plink.eigenvec")


PC1 = PCs[:,2]
PC2 = PCs[:,3]

AFs = np.loadtxt("allele_freqs.frq", skiprows = 1, usecols = 4)


fig1, ax1 = plt.subplots()

ax1.scatter(PC1, PC2, color = "limegreen")
ax1.set_xlabel("PC1")
ax1.set_ylabel("PC2")
ax1.set_title( "Genotypes: First two PCs")
plt.tight_layout()

fig1.savefig("PC_plot.png")

fig2, ax2 = plt.subplots()

ax2.hist(AFs, color = 'hotpink', bins = 80)
ax2.set_xlabel("Allele Frequency")
ax2.set_ylabel("Occurances")
ax2.set_title( "Allele Frequencies")
plt.tight_layout()

fig2.savefig("Allele_freq_plot.png")

gwas_G = pd.read_csv('GS451_gwas_results.assoc.linear', delim_whitespace =True)
gwas_C = pd.read_csv('CB1908_gwas_results.assoc.linear', delim_whitespace =True)

gwas_G = gwas_G.loc[gwas_G['TEST'] == 'ADD', :]
gwas_C = gwas_C.loc[gwas_C['TEST'] == 'ADD', :]

gwas_G['-log10_P'] = -(np.log10(gwas_G['P']))
gwas_C['-log10_P'] = -(np.log10(gwas_C['P']))


fig3, axs = plt.subplots(2,1, figsize = [13, 8])

axs[0].scatter(gwas_G.index, gwas_G['-log10_P'], c=gwas_G['P']< 1e-5, cmap = 'Dark2')
axs[0].axhline(-np.log10(1e-5), color = 'black', linestyle='--', label='Threshold (1e-5)')
#axs[0].set_yscale('log')
axs[0].set_xlabel('SNP Loc')
axs[0].set_ylabel('-log10(P-val)')
axs[0].set_title('GS451_IC50')
axs[0].grid(True, linestyle = '--', alpha = 0.7)
axs[0].set_ylim(0,10)
axs[0].legend()

#axs[1].scatter(gwas_C['BP'], gwas_C['-log10_P'], c=gwas_C['P']< 1e-5 , cmap = 'Set2')
axs[1].scatter(gwas_C.index, gwas_C['-log10_P'], c=gwas_C['P']< 1e-5 , cmap = 'Set2')
axs[1].axhline(-np.log10(1e-5), color = 'black', linestyle='--', label='Threshold (1e-5)')
#axs[1].set_yscale('log')
axs[1].set_xlabel('SNP Loc')
axs[1].set_ylabel('-log10(P-val)')
axs[1].set_title('CB1908_IC50')
axs[1].grid(True, linestyle = '--', alpha = 0.7)
axs[1].set_ylim(0,10)
axs[1].legend()
plt.tight_layout()
fig3.savefig("Manhattans.png")

fig4, ax4 = plt.subplots()
maxP = np.max(gwas_G['-log10_P'])
rowID = gwas_G[gwas_G['-log10_P'] == maxP]
snpID = rowID.loc[:,'SNP'].values[0]

maxP2 = np.max(gwas_C['-log10_P'])
rowID2 = gwas_C[gwas_C['-log10_P'] == maxP2]
snpID2 = rowID2.loc[:,'SNP'].values[0]

GT_vcf = pd.read_csv('genotypes.vcf', delimiter = '\t', skiprows = 27)
GOI = GT_vcf[GT_vcf['ID']==snpID]

POI = pd.read_csv('GS451_IC50.txt', delim_whitespace = True)

wt = []
het = []
hom = []

plt_me = [wt, het, hom]

for i in range(len(GOI.values[0])):
    if GOI.values[0][i]== '0/0':
       wt.append(POI.iloc[i-9,2])
    if GOI.values[0][i]== '0/1':
       het.append(POI.iloc[i-9,2])
    if GOI.values[0][i]== '1/1':
       hom.append(POI.iloc[i-9,2])

for i in range(len(plt_me)):
    plt_me[i] = [x for x in plt_me[i] if str(x) != 'nan']

ax4.boxplot(plt_me)
ax4.set_title( "Genotypes and their phenotypes")
ax4.set_xlabel('Genoype')
ax4.set_ylabel('Phenotype')
plt.savefig("Boxplot.png")

print(snpID)
print(snpID2)





