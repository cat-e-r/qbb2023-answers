EXERCISE 1.1
plink --noweb --vcf genotypes.vcf --pca 10

EXERCISE 2.1
plink --noweb --vcf genotypes.vcf --freq --out allele_freqs

EXERCISE 3.1
plink --vcf genotypes.vcf --linear --pheno GS451_IC50.txt --covar plink.eigenvec --allow-no-sex --out GS451_gwas_results

plink --vcf genotypes.vcf --linear --pheno CB1908_IC50.txt --covar plink.eigenvec --allow-no-sex --out CB1908_gwas_results

3.4
GS451_IC50 - human gene ZNF826: Predicted to enable DNA-binding transcription factor activity, so you may lose expression of some gene(s).
CB1908_IC50 - human gene DIP2B: The encoded protein contains a binding site for the transcriptional regulator DNA methyltransferase 1 associated protein 1, so it might mess with gene silencing.
