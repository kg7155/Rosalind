solution = open('solutions/08-solution.txt', 'w')

with open('datasets/08-dataset.txt') as fp:
    dna = fp.readline().rstrip()

rna = dna.replace('T', 'U')

solution.write(rna)
solution.close()