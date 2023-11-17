#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np

baitmap, washtxt, output = sys.argv[1:4]

f = open(output, 'w')
f.write('track type=interact name="pCHIC" description="Chromatin interactions" useScore=on maxHeightPixels=200:100:50 visibility=full\n')


baits = pd.read_table(baitmap, delim_whitespace = True, header = None, names = ['chrom', 'start', 'end', 'ref_num', 'gene'])
baits['id'] = 'chr' + baits['chrom'].astype(str) + ',' + baits['start'].astype(str) + ',' + baits['end'].astype(str)
baits.index = baits['id']
#print(baits)

ucsc_data = []
max_val = None
with open(washtxt, 'r') as file:
    for line in file:
        line = line.strip().split()
        frag1_pos = line[0]
        frag_1 = line[0].split(',')
        frag2_pos = line[1]
        frag_2 = line[1].split(',')
        
        chrom = frag_1[0]
        start = min(int(frag_1[1]), int(frag_2[1]))
        end = max(int(frag_1[2]), int(frag_2[2]))
        name = '.'
        score = 'NA'
        val = float(line[2])
        exp = '.'
        color = 0
        if frag1_pos in baits.index:
            sourceChrom = frag_1[0]
            sourceStart = frag_1[1]
            sourceEnd = frag_1[2]
            sourceName = baits.loc[frag1_pos, 'gene']
            sourceStrand = '+'
            targetChrom = frag_2[0]
            targetStart = frag_2[1]
            targetEnd = frag_2[2]
            if frag2_pos in baits.index:
                targetChrom = frag_2[0]
                targetStart = frag_2[1]
                targetEnd = frag_2[2]
                targetName = baits.loc[frag2_pos, 'gene']
                targetStrand = '+'
            else:
                targetName = '.'
                targetStrand = '-'
        elif frag2_pos in baits.index:
            sourceChrom = frag_2[0]
            sourceStart = frag_2[1]
            sourceEnd = frag_2[2]
            sourceName = baits.loc[frag2_pos, 'gene']
            sourceStrand = '+'
            targetChrom = frag_1[0]
            targetStart = frag_1[1]
            targetEnd = frag_1[2]
            targetName = '.'
            targetStrand = '-'
        if max_val is None or val > max_val:
            max_val = val
        line_list = [chrom, start, end, name, score, val, exp, color, sourceChrom, sourceStart, sourceEnd, sourceName, sourceStrand, targetChrom, targetStart, targetEnd, targetName, targetStrand]
        ucsc_data.append(line_list)


for interaction in ucsc_data:
    score = int((interaction[5]/max_val)*1000)
    interaction[4] = score
    f.write('\t'.join([str(x) for x in interaction]) + '\n')

second_read =  pd.read_table(output, delim_whitespace = True, skiprows = 1, header=None)
sorted_read = second_read.sort_values(by = second_read.columns[4])
#print(second_read[second_read.columns[4]])
#print(sorted_read[sorted_read.columns[4]])


sorted_read.iloc[0:6, :].to_csv('top_6.txt', header = None, index = None, sep = '\t')

        


