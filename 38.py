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
    F = [[0] * len(states) for i in range(len(ems))]

    # initialize
    for j in range(len(states)):
        e_0 = char_to_idx(ems[0], alphabet)
        prob = E[j][e_0] * 1/len(states)
        F[0][j] = prob
    
    # fill rest
    for i in range(1, len(ems)):
        e_idx = char_to_idx(ems[i], alphabet)
        for l in range(len(states)):
            prob_sum = 0
            for k in range(len(states)):
                prob_sum += F[i-1][k] * T[k][l]
            F[i][l] = E[l][e_idx] * prob_sum
    
    # final prob. is the sum of the last row
    return F, sum(F[len(ems)-1])
#--------------------------------------------------------------------------
# compute the prob. of observed sequence with the backward algorithm

def backward_alg():
    # dynamic programming list, containing backward probs. for each state
    B = [[0] * len(states) for i in range(len(ems))]

    # initialize
    for j in range(len(states)):
        e_last = char_to_idx(ems[-1], alphabet)
        B[-1][j] = 1

    # fill rest
    for i in range(len(ems)-2, -1, -1):
        e_idx = char_to_idx(ems[i+1], alphabet)
        for l in range(len(states)):
            prob_sum = 0
            for k in range(len(states)):
                prob_sum += T[l][k] * E[k][e_idx] * B[i+1][k]
            B[i][l] = prob_sum

    return B
#--------------------------------------------------------------------------
# compute the prob. that the HMM was in state k at step i (for each state and step)

def soft_decoding():
    P = [[0] * len(states) for i in range(len(ems))]

    for i in range(len(P)):
        for j in range(len(P[0])):
            P[i][j] = F[i][j] * B[i][j] / F_prob

    return P

#--------------------------------------------------------------------------

solution = open("solutions/38-solution.txt", 'w')
ems, alphabet, states, T, E = parse_data("datasets/38-dataset.txt")

F, F_prob = forward_alg()
B = backward_alg()
P = soft_decoding()

solution.write("A\tB\n")
for i in range(len(P)):
    for j in range(len(P[0])):
        solution.write("%.4f\t" % P[i][j])
    solution.write('\n')
solution.close()