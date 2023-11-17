
Exercise 1.1:
Rscript runChicago.R raw/PCHIC_data/GM_rep1.chinput,raw/PCHIC_data/GM_rep2.chinput,raw/PCHIC_data/GM_rep3.chinput output --design-dir raw/Design --en-feat-list raw/Features/featuresGM.txt --export-format washU_text

Exercise 1.2:
Do these enrichments make sense to you? Are any surprising? Explain your reasoning briefly for each feature.
- H3K27me3 is a heterochromatin mark, so it is EXPECTED that the promoter is not in heterochromatin.
- H3K4me1 and H3K27ac are associated with euchromatin regions so it's EXPECTED that there is significant overlap at promoter regions.
- CTCF is as EXPECTED at boundary regions at promoters.
- H3K4me3 is known to be at the promoters of regulatory genes so it's EXPECTED that there is significant overlap at promoter regions.
- H3K9me3 is a heterochromatin mark so it's a little SURPRISING that there is significant overlap at promoter regions.

Exercise 2.2:
chr20   25227277    25324806    .   143.80212827149842  5.0 .   0   chr20   25227277    25231213    PYGB    +   chr20   25317055    25324806    .   -
chr20   60635322    60762448    .   143.80212827149842  5.0 .   0   chr20   60756847    60762448    MTG2    +   chr20   60635322    60638149    .   -
chr20   52476392    52560771    .   143.80212827149842  5.0 .   0   chr20   52556648    52560771    AC005220.3  +   chr20   52476392    52480847    .   -
chr20   55627168    55850068    .   143.80212827149842  5.0 .   0   chr20   55627168    55633941    AL117380.1  +   chr20   55839193    55850068    BMP7;RP4-813D12.3   +
chr20   36954175    37001381    .   143.80212827149842  5.0 .   0   chr20   36954175    36958047    CTD-2308N23.2   +   chr20   36998177    37001381    .   -
chr21   33755386    33938278    .   143.80212827149842  5.0 .   0   chr21   33755386    33767163    C21orf119;URB1  +   chr21   33933703    33938278    .   -

Exercise 2.3:
In the top scoring interaction region, ZNF217 (a zinc finger protein which romotes cell proliferation and antagonizes cell death) interacts with BCAS1 (a gene associated with more aggressive tumor phenotypes). This makes a lot of sense since tumors are uncontrolled cell growth. This also makes sense to be happening in an immune response dataset.


