# data
emissions = "xxzzxyzxyzxyzyxxyyyxzxzxxzzxzzyzzyxzxyyxzzxyyxyxxz"
alphabet = "xyz"
hidden_path = "BABABABAAABABBAAAAABBBBAABBABABAABAAABABBBBABABABB"
states = "AB"
emission_matrix = [[0.2, 0.268, 0.532], [0.49, 0.348, 0.162]]

# 'A':0, 'B':1
states_dict = {}
i = 0
for state in states:
    states_dict[state] = i
    i = i + 1

# 'x':0, 'y':1, 'z':2
symbols_dict = {}
i = 0
for symbol in alphabet:
    symbols_dict[symbol] = i
    i = i + 1

# compute the probability of an outcome (emissions) given the path and emission probabilities
prob = 1
for i in range(len(hidden_path)):
    state_from = states_dict[hidden_path[i]]
    symbol = symbols_dict[emissions[i]]
    prob = prob * emission_matrix[state_from][symbol]

print(prob)