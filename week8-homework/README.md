
Exercise 1.1:
Rscript runChicago.R raw/PCHIC_data/GM_rep1.chinput,raw/PCHIC_data/GM_rep2.chinput,raw/PCHIC_data/GM_rep3.chinput output --design-dir raw/Design --en-feat-list raw/Features/featuresGM.txt --export-format washU_text

Exercise 1.2:
Do these enrichments make sense to you? Are any surprising? Explain your reasoning briefly for each feature.
- H3K27me3 is a heterochromatin mark, so it is EXPECTED that the promoter is not in heterochromatin.
- H3K4me1 and H3K27ac are associated with euchromatin regions so it's EXPECTED that there is significant overlap at promoter regions.
- CTCF is as EXPECTED at boundary regions at promoters.
- H3K4me3 is known to be at the promoters of regulatory genes so it's EXPECTED that there is significant overlap at promoter regions.
- H3K9me3 is a heterochromatin mark so it's a little SURPRISING that there is significant overlap at promoter regions.


