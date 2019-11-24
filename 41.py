from Bio import SeqIO
from Bio.Seq import Seq
#--------------------------------------------------------------------------------------
# reverse palindrome is a DNA string that is equal to its reverse complement

def find_reverse_palindromes(s):
    rev_pals = []
    for l in lens:
        for i in range(len(s)-l+1):
            ss = Seq(s[i:i+l])
            rc = ss.reverse_complement()
            if (ss == rc):
                rev_pals.append((i+1, l))
    return rev_pals
#--------------------------------------------------------------------------------------

solution = open("solutions/41-solution.txt", 'w')

dna_strings = []
for s in SeqIO.parse("datasets/41-dataset.txt", "fasta"):
    dna_strings.append(s.seq)

dna = str(dna_strings[0])
# find reverse palindromes of length between 4 and 12
lens = range(4, 13)
rev_pals = find_reverse_palindromes(dna)

for rp in rev_pals:
    solution.write("%s %s\n" % (str(rp[0]), str(rp[1])))
solution.close()