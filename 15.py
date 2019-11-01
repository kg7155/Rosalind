# create a FASTA dict: key is a FASTA ID string (Rosalind_xxxx) and value is a DNA string
def create_fasta_dict(lines):
    fasta_dict = {}
    for i in range(0,len(lines)):
        if (lines[i][0] == '>'):
            line = lines[i][1:]
            fasta_dict[line] = ""
        else:
            fasta_dict[line] = fasta_dict[line] + lines[i]
    return fasta_dict

#--------------------------------------------------------

solution = open('solutions/15-solution.txt', 'w')

data = open('datasets/15-dataset.txt')
lines = data.readlines()

fasta_dict = create_fasta_dict(lines)

for k in fasta_dict:
    s = fasta_dict[k].replace('\n', '')

# Knuth-Moriss-Pratt algorithm (preprocessing)
n = len(s)
i = 0
j = -1
b = [0] * (n+1)
b[i] = j
while (i < n):
    while (j >= 0 and s[i] != s[j]):
        j = b[j]
    i = i + 1
    j = j + 1
    b[i] = j

solution.write(' '.join(map(str, b[1:])))
solution.close()