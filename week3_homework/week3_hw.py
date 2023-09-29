#!/usr/bin/env python

import numpy as np
import sys
import pandas as pd
from fasta import readFASTA

def my_read_files(seq_file, score_sys):

    input_sequences = readFASTA(open(seq_file))
    
    seq1_id, sequence1 = input_sequences[0]
    seq2_id, sequence2 = input_sequences[1]

    score_scheme = pd.read_csv(score_sys, delim_whitespace=True)

    return seq1_id, sequence1, seq2_id, sequence2, score_scheme

FASTA_file = sys.argv[1]
scoring_sys = sys.argv[2]


sq1_name, sq1, sq2_name, sq2, scoring_matrix = my_read_files(FASTA_file, scoring_sys)


gap_penalty = float(sys.argv[3])

#Make F-matrix

F_matrix = np.zeros((len(sq1)+1, len(sq2)+1))
tb_matrix = np.zeros((len(sq1)+1, len(sq2)+1), str)


for i in range(len(sq1)+1):
    F_matrix[i,0] = i * gap_penalty
    tb_matrix[i,0] = 'v'

for j in range(len(sq2)+1):
    F_matrix[0,j] = j * gap_penalty
    tb_matrix[0,j] = 'h'

for i in range(1, F_matrix.shape[0]):
    for j in range(1, F_matrix.shape[1]):
        d = F_matrix[i-1,j-1] + scoring_matrix.loc[sq1[i-1],sq2[j-1]]
        h = F_matrix[i, j-1] + gap_penalty
        v = F_matrix[i-1, j] + gap_penalty

        F_matrix[i,j] = max(d,h,v)
        if F_matrix[i,j] == d:
            tb_matrix[i,j] = 'd'
        elif F_matrix[i,j] == h:
            tb_matrix[i,j] = 'h'
        else:
            tb_matrix[i,j] = 'v'

print(F_matrix)
print(tb_matrix)


# # While loops to keep track

# for i in range(0, 10):
#     print(i)

# i = 9
# while i >= 0:
#     print(i)
#     i -= 1

