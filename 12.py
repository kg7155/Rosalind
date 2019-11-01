solution = open('solutions/12-solution.txt', 'w')

with open('datasets/12-dataset.txt') as fp:
    dna_s = fp.readline().rstrip()
    dna_t = fp.readline().rstrip()

# find locations where dna_t is a substring of dna_s
l = len(dna_t)
for i in range(len(dna_s)-l+1):
    subseq = dna_s[i:i+l]
    if (subseq == dna_t):
        solution.write(str(i+1) + ' ')
        
solution.close()