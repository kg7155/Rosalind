from Bio.Seq import Seq, translate
from Bio.Alphabet import generic_dna

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

solution = open('solutions/17-solution.txt', 'w')

with open('datasets/17-dataset.txt') as fp:
    dna_line = fp.readline().rstrip()

proteins = []

# proteins can be found in DNA or its reverse complement
dna = Seq(dna_line, generic_dna)
rev_compl = dna.reverse_complement()

find_proteins(dna)
find_proteins(rev_compl)

# write the longest protein string that can be translated from an ORF
solution.write(str(max(proteins, key=len)))
solution.close()