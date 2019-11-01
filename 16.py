from collections import Counter
import numpy as np

#--------------------------------------------------------

solution = open('solutions/16-solution.txt', 'w')

with open('datasets/16-dataset.txt') as fp:
    dna_s = fp.readline().rstrip()
    gc_line = fp.readline().rstrip()

gcs = list(map(float, gc_line.split(' ')))

for gc in gcs:
    prob = 1
    for nucleotide in dna_s:
        if (nucleotide == 'G' or nucleotide == 'C'):
            pgc = gc / 2
            prob = prob * pgc
        else:
            pta = (1 - gc) / 2
            prob = prob * pta
    prob = np.round(np.log10(prob), 3) 
    solution.write(str(prob) + ' ')

solution.close()