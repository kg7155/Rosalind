from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

#--------------------------------------------------------------------------
# construct a cyclic superstring of minimal length containing the edges

def construct_cyclic_chromosome(edges):
    cc = ""
    num_edges = len(edges)
    _, to = next(iter(edges.items()))
    to = edges[to]
    i = 0
    while i < num_edges:
        cc += to[-1]
        to = edges[to]
        i += 1
    return cc
#--------------------------------------------------------------------------
# construct an adjacency list corresponding to the de Bruijn graph

def de_bruijn(dnas):
    edges = dict()
    for dna in dnas:
        r = str(dna)
        edges[r[:k]] = r[1:]
    return edges
#--------------------------------------------------------------------------

solution = open("solutions/33-solution.txt", 'w')
with open("datasets/33-dataset.txt", 'r') as f:
        S = [Seq(line.rstrip(), generic_dna) for line in f]

k = len(str(S[0]))-1
edges = de_bruijn(S)
cc = construct_cyclic_chromosome(edges)

solution.write(cc)
solution.close()