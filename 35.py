def parse_data(filename):
    D = [] # distance matrix
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        for _ in range(n):
            line = f.readline()
            D.append(list(map(float, line.split())))
    # distances list (i, j, val)
    dists = []
    for i in range(n):
        for j in range(i+1, n):
            dists.append((i, j, D[i][j]))
    return n, dists
#--------------------------------------------------------------------------
# return all distinct nodes from the list

def find_distinct_nodes(dists):
    nodes = set()
    for (i, j, val) in dists:
        nodes.add(i)
        nodes.add(j)
    return nodes
#--------------------------------------------------------------------------
# compute Q-distances from distances

def compute_q_dists(dists):
    q_dists = []
    nodes = find_distinct_nodes(dists)
    # for each node compute total distance from other nodes
    total_distances = []
    for node in nodes:
        td = 0
        for (i, j, val) in dists:
            if (i == node or j == node):
                td += val
        total_distances.append((node, td)) 
    # compute Q-distances
    for (i, j, val) in dists:
        tdi = [x[1] for x in total_distances if (x[0]==i)][0]
        tdj = [x[1] for x in total_distances if (x[0]==j)][0]
        qd = (len(nodes)-2) * val - tdi - tdj
        q_dists.append((i, j, qd))
    return q_dists, total_distances
#--------------------------------------------------------------------------
# return indices of the min. element in a list of tuples: (i, j, val)

def find_min(q_dists):
    min_indices = [q_dists[0][0], q_dists[0][1]]
    min_val = q_dists[0][2]
    for (i, j, val) in q_dists:
        if (val < min_val):
            min_indices[0] = i
            min_indices[1] = j
            min_val = val
    return min_indices
#--------------------------------------------------------------------------
# get the distance between node n1 and node n2 from a list

def get_node_dist(n1, n2, dists):
    for (i, j, val) in dists:
        if ((i == n1 and j == n2) or (j == n1 and i == n2)):
            return val
    return -1
#--------------------------------------------------------------------------
# join neighbours and update distance list values

def recompute_dists(dists, total_dists, join_pair, new_node_idx):
    nodes = find_distinct_nodes(dists)
    num_nodes = len(nodes)
    
    n1 = join_pair[0]
    n2 = join_pair[1]
    td_n1 = [x[1] for x in total_dists if (x[0]==n1)][0]
    td_n2 = [x[1] for x in total_dists if (x[0]==n2)][0]
    d_n1n2 = get_node_dist(n1, n2, dists)
    # for each node in joined pair compute distance to the new node 
    d_n1new = 1/2 * d_n1n2 + 1/(2*(num_nodes-2)) * (td_n1-td_n2)
    d_n2new = 1/2 * d_n1n2 + 1/(2*(num_nodes-2)) * (td_n2-td_n1)
    # add those edges to the solutions
    T.append((n1, new_node_idx, d_n1new))
    T.append((n2, new_node_idx, d_n2new))
    # remove joined pair from nodes
    nodes.remove(n1)
    nodes.remove(n2)
    # compute distances to the new node for other nodes as well
    for node in nodes:
        d_n1node = get_node_dist(n1, node, dists)
        d_n2node = get_node_dist(n2, node, dists)
        d = 1/2 * (d_n1node + d_n2node - d_n1n2)
        dists.append((node, new_node_idx, d))
    # remove joined pair distances from the distances list
    dists = [x for x in dists if x[0] != n1 and x[1] != n2]
    dists = [x for x in dists if x[0] != n2 and x[1] != n1]
    # add the last remaining edge to solutions
    if (len(dists) == 1):
        T.append((dists[0]))
    return dists
#--------------------------------------------------------------------------
# neigbour joining algorithm

def join_neighbours(n, dists):
    new_node_idx = n

    while (len(dists) > 1):
        q_dists, total_dists = compute_q_dists(dists)
        join_pair = find_min(q_dists)
        dists = recompute_dists(dists, total_dists, join_pair, new_node_idx)
        new_node_idx += 1
#--------------------------------------------------------------------------

solution = open("solutions/35-solution.txt", 'w')
n, dists = parse_data("datasets/35-dataset.txt")

T = []
join_neighbours(n, dists)

for t in T:
    solution.write("%d->%d:%.3f\n" % (t[0], t[1], t[2]))
for t in T:
    solution.write("%d->%d:%.3f\n" % (t[1], t[0], t[2]))
solution.close()