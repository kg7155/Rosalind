from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

#--------------------------------------------------------------------------
# construct an adjacency list corresponding to the de Bruijn graph

def de_bruijn(dnas):
    edges = []
    for dna in dnas:
        r = str(dna)
        r_rc = str(dna.reverse_complement())
        edges.append((r[:k], r[1:]))
        edges.append((r_rc[:k], r_rc[1:]))
    return edges
#--------------------------------------------------------------------------

solution = open("solutions/32-solution.txt", 'w')
with open("datasets/32-dataset.txt", 'r') as f:
        S = [Seq(line.rstrip(), generic_dna) for line in f]

k = len(str(S[0]))-1
edges = set(de_bruijn(S))

for e in edges:
    solution.write("(%s, %s)\n" % (e[0], e[1]))
solution.close()