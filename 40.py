from Bio import SeqIO
from collections import Counter
#-----------------------------------------------------------------------------------------
# compute the profile matrix representing number of times that each nucleotide occurs
# in the i-th position of input strings

def compute_profile():
    l = len(str(dna_strings[0]))
    P = [[0] * l for i in range(4)]
    for i in range(l):
        s = ""
        for j in range(len(dna_strings)):
            s += dna_strings[j][i]
        sym_count = Counter(s)
        for row_idx in range(len(P)):
            cs = symbols[row_idx]
            if (cs in sym_count):
                P[row_idx][i] = sym_count[cs]
            else:
                P[row_idx][i] = 0
    return P
#-----------------------------------------------------------------------------------------
# compute consensus string (most common symbol at each position from the profile matrix P)

def compute_consensus():
    c = ""
    for j in range(len(P[0])):
        max_val = 0
        max_idx = 0
        for i in range(len(P)):
            if (P[i][j] > max_val):
                max_val = P[i][j]
                max_idx = i
        c += symbols[max_idx]
    return c
#-----------------------------------------------------------------------------------------

solution = open("solutions/40-solution.txt", 'w')

dna_strings = []
for s in SeqIO.parse("datasets/40-dataset.txt", "fasta"):
    dna_strings.append(s.seq)

symbols = "ACGT"
P = compute_profile()
cons = compute_consensus()

solution.write(cons + '\n')
for i in range(len(P)):
    solution.write("%c: " % symbols[i])
    for j in range(len(P[i])):
        solution.write("%d " % P[i][j])
    solution.write('\n')
solution.close()