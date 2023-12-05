#!/usr/bin/env python

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats import multitest
from pydeseq2 import preprocessing
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
import matplotlib.pyplot as plt

# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

counts_df_normed = np.log2(counts_df_normed + 1)

full_design_df = pd.concat([counts_df_normed, metadata], axis=1)

model = smf.ols(formula = 'Q("DDX11L1") ~ SEX', data=full_design_df)
results = model.fit()

#print(results.summary())

slope = results.params[1]
pval = results.pvalues[1]

# Do this for all the genes
# genes = list(full_design_df.columns.values)
# genes = genes[: len(genes)-3]

# all_results = {'Gene_ID': [], 'Slope': [], 'P_Value': []}
# f = open('all_results', 'w')
# f.write('gene\tslope\tpval\n')

# for gene in genes:
#     model = smf.ols(formula = 'Q("'+gene+'") ~ SEX', data=full_design_df)
#     results = model.fit()
#     slope = results.params[1]
#     pval = results.pvalues[1]
#     f.write(f'{gene}\t{slope}\t{pval}\n')

# f.close()

my_df = pd.read_csv("all_results", header=0, index_col=False, sep='\t')
my_df['pval'] = my_df['pval'].fillna(1.0)

my_df["rejected"], my_df['corrected'] = multitest.fdrcorrection(my_df['pval'], alpha =0.10, method = 'indep', is_sorted = False)

#print(my_df)

FDR_hits = my_df.loc[my_df['corrected'] <= 0.1]
FDR_hits_2 = FDR_hits['gene'].tolist()
FDR_hits.to_csv("Ex1hits")

# Now try PyDESeq
dds = DeseqDataSet(
    counts=counts_df,
    metadata=metadata,
    design_factors="SEX",
    n_cpus=4,
)

dds.deseq2()
stat_res = DeseqStats(dds)
stat_res.summary()
results = stat_res.results_df

results['padj'] = results['padj'].fillna(1.0)
#print(results)

ddsFDR_hits = results.loc[results['padj'] <= 0.1]
ddsFDR_hits.to_csv("DeseqDataSet_10percentFDRgenes.txt", header = None, index = None, sep = '\t')
sig_genes = results[(results['padj'] <= 0.1) & (abs(results['log2FoldChange']) < 1)]
sig_genes.to_csv("Ex2hits")
#print(sig_genes)
sg2 = sig_genes.index.tolist()


in_FDR = set(FDR_hits_2)
in_sig_genes = set(sg2)
in_both = in_FDR.intersection(in_sig_genes)
unique = in_FDR.difference(in_sig_genes)

#Jacard index
j_index = len(unique)/len(in_both) * 100
print(j_index)

# volcano plot
plt.figure(figsize=(12, 9))
plt.scatter(results['log2FoldChange'], -np.log10(results['padj']), color='gray', label='Non-Significant')
plt.scatter(sig_genes['log2FoldChange'], -np.log10(sig_genes['padj']), color='coral', label='Significant (FDR<0.1, |log2FC|>1)')

plt.xlabel('log2FoldChange')
plt.ylabel('-log10(padj)')
plt.title('DE Volcano Plot')

plt.axvline(x=0, linestyle='--', color='black', linewidth=0.9)
plt.axhline(y=-np.log10(0.1), linestyle='--', color='black', linewidth=0.9)
plt.legend(loc = 3)

# Save plot
plt.savefig('volc_plt.png')




