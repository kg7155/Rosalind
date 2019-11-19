# data
hidden_path = "BBBBAAAAAABAAABBBAABAAAABBAAAAABBAABABABAABAAAAABA"
states = "AB"
transition_matrix = [[0.531, 0.469], [0.925, 0.075]]

# 'A':0, 'B':1
states_dict = {}
i = 0
for state in states:
    states_dict[state] = i
    i = i + 1

# initial probabilities are equal
init_prob = 1/len(states)

# compute the probability of hidden path
prob = init_prob
for c in range(len(hidden_path)-1):
    state_from = states_dict[hidden_path[c]]
    state_to = states_dict[hidden_path[c+1]]
    prob = prob * transition_matrix[state_from][state_to]

print(prob)