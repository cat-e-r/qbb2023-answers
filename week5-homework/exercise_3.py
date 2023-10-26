#!/usr/bin/env python

import matplotlib.pyplot as plt

read_depths = []
gt_quals = []
allele_freqs = []
effects = []
for line in open("ann_yeast_variants.vcf"):
    if line.startswith('#'):
        continue
    fields = line.rstrip('\n').split('\t')
    for chrom in fields[9:]:
        if chrom.split(':')[2] != '.':
            depth = int(chrom.split(':')[2])
            read_depths.append(depth)
        if chrom.split(':')[1] != '.':
            gt_qual = float(chrom.split(':')[1])
            gt_quals.append(gt_qual)
    var_freq = fields[7].split(';')[3][3:]
    var_freq = var_freq.split(',')[0]
    allele_freq = float(var_freq)
    allele_freqs.append(allele_freq)
    eff_type = fields[7].split(';')[41][5:]
    eff_type = eff_type.split('|')[2]
    eff_type = eff_type.split(',')[0]
    effects.append(eff_type)
    set_effects = []
    counts = []
    for i in set(effects):
        set_effects.append(i)
        counts.append(effects.count(i))

    
#print(allele_freqs)



fig, axs = plt.subplots(1, 4, figsize = [18, 5])
axs[0].set_title( "Read Depths")
axs[0].hist(read_depths, color = 'hotpink', bins = 700)
axs[0].set_xlabel("Read Depth")
axs[0].set_ylabel("Ocurrances")
axs[0].set_xlim(0, 75)
axs[1].set_title( "Genotype Qualities")
axs[1].hist(gt_quals, color = 'limegreen', bins = 100)
axs[1].set_xlabel("Genotype Quality")
axs[1].set_ylabel("Ocurrances")
axs[1].set_ylim(0, 6000)
axs[2].set_title( "Variant Frequencies")
axs[2].hist(allele_freqs, color = 'mediumturquoise', bins = 30)
axs[2].set_xlabel("Variant Frequency")
axs[2].set_ylabel("Ocurrances")
axs[2].set_ylim(0, 8500)
axs[3].set_title( "Variant Effects")
axs[3].bar(set_effects, counts, color = 'dodgerblue')
axs[3].set_xlabel("Variant Frequency")
axs[3].set_ylabel("Ocurrances")
axs[3].tick_params(axis='x', labelrotation = 25)
plt.tight_layout()
plt.show()
fig.savefig("Plots")

