# Hamming distance is the number of corresponding symbols that differ between s1 and s2

def compute_hamming_dist(s1, s2):
    diff = 0
    for i in range(len(s1)):
        if (s1[i] != s2[i]):
            diff = diff + 1
    return diff

#--------------------------------------------------------------------------------------

solution = open('solutions/20-solution.txt', 'w')

with open('datasets/20-dataset.txt') as fp:
    dna_s1 = fp.readline().rstrip()
    dna_s2 = fp.readline().rstrip()

solution.write(str(compute_hamming_dist(dna_s1, dna_s2)))
solution.close()