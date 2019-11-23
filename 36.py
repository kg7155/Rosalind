def parse_data(filename):
    T = [] # initial transition matrix
    E = [] # initial emission matrix
    with open(filename, 'r') as f:
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
# compute the prob. of observed sequence with the forward algorithm

def forward_alg():
    # dynamic programming list, containing forward probs. for each state
    D = [[0] * len(states) for i in range(len(ems))]

    # initialize
    for j in range(len(states)):
        e_0 = char_to_idx(ems[0], alphabet)
        prob = E[j][e_0] * 1/len(states)
        D[0][j] = prob
    
    # fill rest
    for i in range(1, len(ems)):
        e_idx = char_to_idx(ems[i], alphabet)
        for l in range(len(states)):
            prob_sum = 0
            for k in range(len(states)):
                prob_sum += D[i-1][k] * T[k][l]
            D[i][l] = E[l][e_idx] * prob_sum
    
    # final prob. is the sum of the last row
    return sum(D[len(ems)-1])
#--------------------------------------------------------------------------

solution = open("solutions/36-solution.txt", 'w')
ems, alphabet, states, T, E = parse_data("datasets/36-dataset.txt")

prob = forward_alg()
solution.write(str(prob))
solution.close()