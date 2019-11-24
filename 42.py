from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_rna
#--------------------------------------------------------------------------------------
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
#--------------------------------------------------------------------------------------
# remove introns from the DNA string for the purposes of protein translation

def remove_introns(s):
    introns = [str(i) for i in dna_strings[1:]]
    for intron in introns:
        s = s.replace(intron, '')
    return s
#--------------------------------------------------------------------------------------
# translate RNA string into protein string (each codon into aminoacid)

def translate_rna(rna):
    protein = ''
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        aminoacid = codons_dict[codon]
        if (aminoacid != "Stop"):
            protein = protein + aminoacid
    return protein
#--------------------------------------------------------------------------------------

solution = open("solutions/42-solution.txt", 'w')

dna_strings = []
for s in SeqIO.parse("datasets/42-dataset.txt", "fasta"):
    dna_strings.append(s.seq)

dna = dna_strings[0]
codons_dict = read_rna_table()

exons = Seq(remove_introns(str(dna)), generic_dna)
rna = exons.transcribe()
protein = translate_rna(rna)

solution.write(protein)
solution.close()