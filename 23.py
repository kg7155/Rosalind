from Bio import SeqIO

#--------------------------------------------------------------------------------------
# read BLOSUM62 scoring matrix, used in alignment problems considering protein strings
# return matrix and symbols lookup dict

def read_blosum_table():
    f = open('helpers/BLOSUM62.txt')
    lines = f.readlines()
    
    # 'A': 0, 'C': 1, 'D': 2...
    symbols_dict = {}
    symbols = lines[0].rstrip().split(' ')
    i = 0
    for symbol in symbols:
        symbols_dict[symbol] = i
        i = i + 1

    n = len(symbols_dict)
    B = [[0] * n for i in range(n)]
    for i in range(n):
        scores = lines[i+1].rstrip().split(' ')
        for j in range(n):
            B[i][j] = int(scores[j])
    return B, symbols_dict

#--------------------------------------------------------------------------------------
# initialize and return dynamic programming table M

def initialize():
    # create a matrix M of sizes w x h
    M = [[0] * w for i in range(h)]
    # fill entries in the first column and row (punishments for introducing an indel)
    for i in range(h):
        M[i][0] = -5*i
    for j in range(w):
        M[0][j] = -5*j
    return M

#--------------------------------------------------------------------------------------
# fill dynamic programming table M based on score function

def compute_entries():
    for i in range(1, h):
        for j in range(1, w):
            [s_v, s_h, s_d] = compute_scores(i, j)
            scores = [s_v, s_h, s_d]
            best_score_val = max(scores)
            M[i][j] = best_score_val

#--------------------------------------------------------------------------------------
# compute scores for all different moves (vertical, horizontal, diagonal)

def compute_scores(i, j):
    s_v = M[i-1][j] + get_score(s[i], '-')
    s_h = M[i][j-1] + get_score('-', t[j])
    s_d = M[i-1][j-1] + get_score(s[i], t[j])

    return [s_v, s_h, s_d]

#--------------------------------------------------------------------------------------
# compare symbols and return score based on scoring function

def get_score(a, b):
    if (a == '-' or b == '-'):
        return -5
    
    i = symbols_dict[a]
    j = symbols_dict[b]
    return B[i][j]

#--------------------------------------------------------------------------------------

solution = open('solutions/23-solution.txt', 'w')

records = []
for record in SeqIO.parse("datasets/23-dataset.txt", "fasta"):
    records.append(str(record.seq))

s = '-' + records[0]
t = '-' + records[1]

w = len(t)
h = len(s)

# BLOSUM62 scoring matrix
B, symbols_dict = read_blosum_table()

# Needleman-Wunsch algorithm for finding optimal global alignment of two strings
M = initialize()
compute_entries()

solution.write(str(M[h-1][w-1]))
solution.close()