solution = open('solutions/09-solution.txt', 'w')

with open('datasets/09-dataset.txt') as fp:
    dna = fp.readline().rstrip()

# first reverse the symbols in DNA
rev_compl = list(dna[::-1])

compl_dict = {
    'A':'T',
    'T':'A',
    'C':'G',
    'G':'C'
}

# now replace symbols with complements
for i in range(0, len(rev_compl)):
    symbol = rev_compl[i]
    rev_compl[i] = compl_dict[symbol]
    
solution.write(''.join(rev_compl))
solution.close()