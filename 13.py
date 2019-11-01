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

#---------------------------------------------------------------------------
# create a dict: key is a k-mer of a DNA string and value is its frequency
def k_mer_composition(k, dna):
    comp_dict = {}
    for i in range(len(dna)-k+1):
        subseq = dna[i:i+k]
        if (subseq in comp_dict):
            comp_dict[subseq] = comp_dict[subseq] + 1
        else:
            comp_dict[subseq] = 1
    return comp_dict

#---------------------------------------------------------------------------

solution = open('solutions/13-solution.txt', 'w')
data = open('datasets/13-dataset.txt')
lines = data.readlines()

fasta_dict = create_fasta_dict(lines)

for k in fasta_dict:
    dna_string = fasta_dict[k].replace('\n', '')

four_mer_comp_dict = k_mer_composition(4, dna_string)

# write frequencies of a sorted 4-mer composition dict
for key in sorted(four_mer_comp_dict.keys()):
    solution.write(str(four_mer_comp_dict[key]) + ' ')

solution.close()