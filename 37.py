def parse_data(filename):
    with open(filename, 'r') as f:
        ems = f.readline().strip()
        f.readline() # "--------"
        alphabet = "".join(f.readline().split())
        f.readline() # "--------"
        path = f.readline().strip()
        f.readline() # "--------"
        states = "".join(f.readline().split())
    return ems, alphabet, path, states
#--------------------------------------------------------------------------
# estimate transition matrix T and emission probabilities E 
# from sequences of emitted symbols (ems) and hidden states (path)

def estimate_parameters():
    T = [[0] * len(states) for i in range(len(states))]
    E = [[0] * len(alphabet) for i in range(len(states))]

    for i in range(len(states)):
        for j in range(len(states)):
            c_ij = 0
            for k in range(len(path)-1):
                if (path[k] == states[i] and path[k+1] == states[j]):
                    c_ij += 1
            c_all = path[:len(path)-1].count(states[i])
            if (c_all == 0):
                T[i][j] = 1 / len(states)
            else:
                T[i][j] = c_ij / c_all

    for i in range(len(states)):
        for j in range(len(alphabet)):
            mask = [1 if k==states[i] else 0 for k in path]
            c_j = 0
            for k in range(len(ems)):
                if (ems[k] == alphabet[j] and mask[k]):
                    c_j += 1
            c_p = path.count(states[i])
            if (c_p == 0):
                E[i][j] = 1 / len(states)
            else:
                E[i][j] = c_j / c_p
    
    return T, E
#--------------------------------------------------------------------------

solution = open("solutions/37-solution.txt", 'w')
ems, alphabet, path, states = parse_data("datasets/37-dataset.txt")

T, E = estimate_parameters()

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