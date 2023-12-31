#!/usr/bin/env python

import sys
import scanpy as sc
import numpy
import matplotlib.pyplot as plt


def main():
    sc.settings.verbosity = 3
    sc.logging.print_header()
    adata = sc.read_10x_mtx('filtered_gene_bc_matrices/hg19/',
                            var_names='gene_symbols', cache=True)

    adata.var_names_make_unique()

    sc.tl.pca(adata, svd_solver='arpack')
    raw = adata.copy()
    #sc.pl.pca(adata, title='Unfiltered', save="_unfiltered.pdf")

    print("# cells, # genes before filtering:", adata.shape)
    sc.pp.filter_cells(adata, min_genes=200)
    sc.pp.filter_genes(adata, min_cells=3)
    print("# cells, # genes after filtering:", adata.shape)

    adata.var['mt'] = adata.var_names.str.startswith('MT-')
    sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None,
                               log1p=False, inplace=True)
    # sc.pl.violin(adata, ['n_genes_by_counts', 'total_counts', 'pct_counts_mt'],
    #         jitter=0.4, multi_panel=True)
    
    adata = adata[adata.obs.n_genes_by_counts < 2500, :]
    adata = adata[adata.obs.pct_counts_mt < 5, :]
    print("# cells, # genes after MT filtering:", adata.shape)
    #sc.pl.highest_expr_genes(adata, n_top=20)

    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)

    sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3,
                                min_disp=0.5)
    #sc.pl.highly_variable_genes(adata)
    adata.write("filtered_data.h5")

    adata.raw = adata
    adata = adata[:, adata.var.highly_variable]
    print("# cells, # genes after variability filtering:", adata.shape)

    sc.pp.regress_out(adata, ['total_counts', 'pct_counts_mt'])
    sc.pp.scale(adata, max_value=10)

    sc.tl.pca(adata, svd_solver='arpack')
    #sc.pl.pca_variance_ratio(adata, log=True)
    #sc.pl.pca(adata, color='CST3')

    #fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    #sc.pl.pca(raw, ax=ax[0], title="Uniltered", show=False)
    #sc.pl.pca(adata, ax=ax[1], title="Filtered", show=False)
    #plt.tight_layout()
    #plt.savefig("pca.pdf")
    #plt.close()

    adata.write('variable_data.h5')

main()

# Read the 10x dataset filtered down to just the highly-variable genes
adata = sc.read_h5ad("variable_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 

sc.pp.neighbors(adata, n_neighbors = 10, n_pcs = 40)
sc.tl.leiden(adata)

sc.tl.umap(adata, maxiter = 900)
sc.tl.tsne(adata)

# #Plot UMAP and tSNE clustering
# fig, ax = plt.subplots(ncols = 2)
# sc.pl.umap(adata, color='leiden', title = "UMAP Plot", show = False, ax=ax[0])
# sc.pl.tsne(adata, color='leiden', title = "tSNE Plot", show = False, ax=ax[1])
# plt.tight_layout()
# plt.savefig("UMAP_tSNE_plots.png")

wilcoxon_adata = sc.tl.rank_genes_groups(adata, method = 'wilcoxon', groupby = 'leiden', use_raw = True, copy = True)
#wilcoxon_adata = adata.copy()
#print(wilcoxon_adata.rank_genes_groups)

logreg_adata = sc.tl.rank_genes_groups(adata, method = 'logreg', groupby = 'leiden', use_raw = True, copy = True)
#logreg_adata = adata.copy()

sc.pl.rank_genes_groups(wilcoxon_adata, n_genes = 25, title='Wilcoxon Marker Genes Rank', sharey=False, show=False, use_raw=True)
plt.savefig('gene_ranks_wilcoxon.png')

sc.pl.rank_genes_groups(logreg_adata, n_genes = 25, title = 'Logreg Marker Genes Rank', sharey=False, show=False, use_raw=True)
plt.savefig('gene_ranks_logreg.png')

#ex 3
leiden = adata.obs['leiden']
umap = adata.obsm['X_umap']
tsne = adata.obsm['X_tsne']
adata = sc.read_h5ad('filtered_data.h5')
adata.obs['leiden'] = leiden
adata.obsm['X_umap'] = umap
adata.obsm['X_tsne'] = tsne

adata.write('filtered_clustered_data.h5')

adata = sc.read_h5ad("filtered_clustered_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 

marker_genes = ['MS4A1', 'LYZ', 'GNLY']

sc.pl.umap(adata, color= marker_genes, title = ["MS4A1 UMAP", "LYZ UMAP", "GNLY UMAP"], show = False)
plt.tight_layout()
plt.savefig("gene_marker_clusters.png")

adata.rename_categories('leiden', ['0', 'Myeloid Cells', 'B-cell', '3', '4', 'NK Cells', '6', '7'])

sc.pl.umap(adata, color='leiden', title = "UMAP Plot", show = False)
plt.tight_layout()
plt.savefig("label_umap_clusters.png")






