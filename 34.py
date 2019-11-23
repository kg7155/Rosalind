from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
#--------------------------------------------------------------------------
# find all circular strings assembled by complete cycles in the de Bruijn graph

def traverse_graph(start_node, path, d):
    # check for a complete cycle
    edges_sum = 0
    for _, val in edges.items():
        for e in val:
            edges_sum += e[1]
    # if all edges were traversed, the path is one of the solutions
    if (edges_sum == len(S)-1):
        circular_strings.add(path[:-k])

    for i in range(len(edges[start_node])):
        e = edges[start_node][i]
        if (e[1] == 0):
            edges[start_node][i][1] = 1
            traverse_graph(e[0], path+e[0][-1:], d-1)
            edges[start_node][i][1] = 0
    
#--------------------------------------------------------------------------
# construct an adjacency list corresponding to the de Bruijn graph

def de_bruijn(dnas):
    edges = dict()
    for dna in dnas:
        r = str(dna)
        start = r[:k]
        val = r[1:]
        if (start in edges):
            edges[start].append([val, 0])
        else:
            vals = [[val, 0]]
            edges[start] = vals 
    return edges
#--------------------------------------------------------------------------

solution = open("solutions/34-solution.txt", 'w')
with open("datasets/34-dataset.txt", 'r') as f:
        S = [Seq(line.rstrip(), generic_dna) for line in f]

k = len(str(S[0]))-1
edges = de_bruijn(S)

# number of all possible paths
num_paths = len(edges.keys())
path = str(S[0])
s = path[1:k+1]
edges[path[:k]].remove([s,0])

circular_strings = set()
traverse_graph(s, path, num_paths+k+1)

for cs in circular_strings:
    solution.write(str(cs) + "\n")
solution.close()