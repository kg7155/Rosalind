from collections import Counter

#--------------------------------------------------------

def computeGC(dna_string):
    nucleotides_dict = Counter(dna_string)
    GC = nucleotides_dict['G'] + nucleotides_dict['C']
    return GC/sum(nucleotides_dict.values())

#--------------------------------------------------------

solution = open('solutions/10-solution.txt', 'w')
data = open('datasets/10-dataset.txt')
lines = data.readlines()

# save data in a dict, where key is a FASTA ID string (Rosalind_xxxx) and value is a DNA string
fasta_dict = {}
for i in range(0,len(lines)):
    if (lines[i][0] == '>'):
        line = lines[i][1:]
        fasta_dict[line] = ""
    else:
        fasta_dict[line] = fasta_dict[line] + lines[i]

# find highest GC-content of a DNA string
highestGC = 0
highestID = ''
for k in fasta_dict:
    dna = fasta_dict[k].replace('\n','')
    GC = computeGC(dna)
    if (GC > highestGC):
        highestGC = GC
        highestID = k.replace('>','')

solution.write(highestID + str(highestGC*100))
solution.close()