from Bio import SeqIO

#--------------------------------------------------------------------------------------
# p-distance is the proportion of corresponding symbols that differ between s1 and s2

def compute_p_dist(s1, s2):
    diff = 0
    for i in range(len(s1)):
        if (s1[i] != s2[i]):
            diff = diff + 1
    return diff/len(s1)

#--------------------------------------------------------------------------------------

solution = open("solutions/19-solution.txt", 'w')

dna_strings = []
for s in SeqIO.parse("datasets/19-dataset.txt", "fasta"):
    dna_strings.append(s.seq)

n = len(dna_strings)
dist_mat = [[0] * n for i in range(n)]

for row in range(n):
    for col in range(n):
        if (row == col):
            dist_mat[row][col] = 0
        else:
            dist_mat[row][col] = compute_p_dist(dna_strings[row], dna_strings[col])

for row in range(n):
    for col in range(n):
        solution.write(str(dist_mat[row][col]) + ' ')
    solution.write('\n')
solution.close()