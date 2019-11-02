from Bio.Seq import Seq, translate
from Bio.Alphabet import generic_dna

#--------------------------------------------------------
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
# trim a DNA sequence so it is divisible by 3

def trim_dna(dna):
    t_pos = len(dna) - len(dna) % 3
    return dna[:t_pos]
#--------------------------------------------------------
# find proteins in a DNA sequence

def find_proteins(dna):
    # for every possible start of ORF
    for offset in range(0,3):
        rna = trim_dna(dna[offset:]).translate()
        # find possible starts of a protein (in RNA the start is 'M')
        start_options = [i for i, c in enumerate(rna) if c == 'M']
        # for every start find the end (in RNA the end is '*')
        # if there is an end, the protein was found
        for start in start_options:
            for p in range(start, len(rna)):
                if (rna[p] == '*'):
                    proteins.append(rna[start:p])
                    break
            
#--------------------------------------------------------

solution = open('solutions/18-solution.txt', 'w')

data = open('datasets/18-dataset.txt')
lines = data.readlines()

fasta_dict = create_fasta_dict(lines)

for k in fasta_dict:
    dna_line = fasta_dict[k].replace('\n', '')

proteins = []

# proteins can be found in DNA or its reverse complement
dna = Seq(dna_line, generic_dna)
rev_compl = dna.reverse_complement()

find_proteins(dna)
find_proteins(rev_compl)

proteins = list(set(proteins))
# write distinct protein strings that can be translated from an ORF
for protein in proteins:
    solution.write(str(protein) + '\n')
solution.close()