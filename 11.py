def read_rna_table():
    rna_table_file = open('helpers/RNA-codon-table.txt')
    lines = rna_table_file.readlines()
    codons_dict = {}
    for line in lines:
        line_split = line.split(' ')
        codon = line_split[0]
        aminoacid = line_split[1].rstrip()
        codons_dict[codon] = aminoacid
    return codons_dict

#--------------------------------------------------------

solution = open('solutions/11-solution.txt', 'w')

with open('datasets/11-dataset.txt') as fp:
    rna = fp.readline().rstrip()

codons_dict = read_rna_table()

# translate codons into a language of 20 aminoacids
protein_string = ''
for i in range(0, len(rna), 3):
    codon = rna[i:i+3]
    aminoacid = codons_dict[codon]
    if (aminoacid != "Stop"):
        protein_string = protein_string + aminoacid

solution.write(protein_string)
solution.close()