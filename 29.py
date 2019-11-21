def parse_data(filename):
    T = [] # transition matrix
    E = [] # emission matrix
    with open(filename, 'r') as f:
        ems = f.readline().strip()
        f.readline() # "-----"
        alphabet = "".join(f.readline().split())
        f.readline() # "-----"
        states = "".join(f.readline().split())
        f.readline() # "-----"
        f.readline() # T header
        for _ in range(len(states)):
            t_line = f.readline()
            T.append(list(map(float, t_line.split()[1:])))
        f.readline() # "-----"
        f.readline() # E header
        for _ in range(len(states)):
            e_line = f.readline()
            E.append(list(map(float, e_line.split()[1:])))
    return ems, alphabet, states, T, E
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
solution = open('solutions/29-solution.txt', 'w')

# parse data
ems, alphabet, states, T, E = parse_data("datasets/29-dataset.txt")

# compute most probable path using Viterbi algorithm
path = viterbi()

solution.write(path)
solution.close()