def parse_data(filename):
    T = [] # initial transition matrix
    E = [] # initial emission matrix
    with open(filename, 'r') as f:
        num_it = int(f.readline().strip())
        f.readline() # "--------"
        ems = f.readline().strip()
        f.readline() # "--------"
        alphabet = "".join(f.readline().split())
        f.readline() # "--------"
        states = "".join(f.readline().split())
        f.readline() # "--------"
        f.readline() # T header
        for _ in range(len(states)):
            t_line = f.readline()
            T.append(list(map(float, t_line.split()[1:])))
        f.readline() # "--------"
        f.readline() # E header
        for _ in range(len(states)):
            e_line = f.readline()
            E.append(list(map(float, e_line.split()[1:])))
    return num_it, ems, alphabet, states, T, E
#--------------------------------------------------------------------------
# helper function to get idx of emission symbol or state
# 'A':0, 'B':1 ...
# 'x':0, 'y':1 ...

def char_to_idx(c, string):
    for i in range(len(string)):
        if (c == string[i]):
            return i
    return -1
#--------------------------------------------------------------------------
# compute most probable path using Viterbi algorithm

def viterbi():
    # dynamic programming list
    # each state: (prob, max_idx)
    D = []

    # initialize
    probs = []
    for j in range(len(states)):
        e_0 = char_to_idx(ems[0], alphabet)
        prob = E[j][e_0] * 1/len(states)
        probs.append((prob, j))
     
    D.append(probs)
    
    # fill rest
    for i in range(1, len(ems)):
        line_probs = []
        for j in range(len(states)):
            e = char_to_idx(ems[i], alphabet)
            state_probs = []
            # compute all probs and find max
            max_prob = 0
            max_idx = -1
            for k in range(len(states)):
                prob = D[i-1][k][0] * T[k][j]
                if (prob > max_prob):
                    max_prob = prob
                    max_idx = k
                state_probs.append((prob, k))
            line_probs.append((E[j][e] * max_prob, max_idx))
        D.append(line_probs)

    # backtrack
    path = ""
    pos = len(ems)-1
    start_state = max(D[pos], key=lambda x:x[0])[1]
    path = states[start_state]

    while (pos > 0):
        start_state = D[pos][start_state][1]
        path = states[start_state] + path
        pos = pos - 1
        
    return path
#--------------------------------------------------------------------------
# recompute transition and emission matrix using inferred path

def recompute_TE():
    for i in range(len(states)):
        for j in range(len(states)):
            c_ij = 0
            for k in range(len(path)-1):
                if (path[k] == states[i] and path[k+1] == states[j]):
                    c_ij += 1
            c_all = path[:len(path)-1].count(states[i])
            T[i][j] = c_ij / c_all

    for i in range(len(states)):
        for j in range(len(alphabet)):
            mask = [1 if k==states[i] else 0 for k in path]
            c_j = 0
            for k in range(len(ems)):
                if (ems[k] == alphabet[j] and mask[k]):
                    c_j += 1
            E[i][j] = c_j / path.count(states[i])
#--------------------------------------------------------------------------

solution = open("solutions/30-solution.txt", 'w')

num_it, ems, alphabet, states, T, E = parse_data("datasets/30-dataset.txt")

for i in range(num_it):
    path = viterbi()
    recompute_TE()

solution.write('\t')
for state in states:
    solution.write(state + '\t')
solution.write('\n')
for i in range(len(T)):
    solution.write(states[i] + '\t')
    for j in range(len(T[i])):
        solution.write("%.3f\t" % T[i][j])
    solution.write('\n')

solution.write("--------\n\t")
for symbol in alphabet:
    solution.write(symbol + '\t')
solution.write('\n')
for i in range(len(E)):
    solution.write(states[i] + '\t')
    for j in range(len(E[i])):
        solution.write("%.3f\t" % (E[i][j]))
    solution.write('\n')