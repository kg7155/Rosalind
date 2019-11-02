from Bio import SeqIO

#--------------------------------------------------------------------------
# initialize and return dynamic programming table M

def initialize():
    # create a matrix M of sizes w x h
    M = [[0] * w for i in range(h)]
    # same for directions used to trace-back an optimal alignment
    directions = [[0] * w for i in range(h)]
    # fill entries in the first column and row (punishments for introducing an indel)
    for i in range(h):
        M[i][0] = -2*i
    for j in range(w):
        M[0][j] = -2*j
    return M, directions

#--------------------------------------------------------------------------
# fill dynamic programming table M based on score function

def compute_entries():
    for i in range(1, h):
        for j in range(1, w):
            [s_v, s_h, s_d] = compute_scores(i, j)
            scores = [s_v, s_h, s_d]
            best_score_val = max(scores)
            best_score_dir = scores.index(best_score_val)
            directions[i][j] = best_score_dir
            M[i][j] = best_score_val

#--------------------------------------------------------------------------
# compute scores for all different moves (vertical, horizontal, diagonal)

def compute_scores(i, j):
    s_v = M[i-1][j] + get_score(s[i], '-')
    s_h = M[i][j-1] + get_score('-', t[j])
    s_d = M[i-1][j-1] + get_score(s[i], t[j])

    return [s_v, s_h, s_d]

#--------------------------------------------------------------------------
# compare symbols and return score based on scoring function

def get_score(a, b):
    if (a == '-' or b == '-'):
        return -2
    elif (a != b):
        return -1
    else:
        return 2

#--------------------------------------------------------------------------
# reconstruct the optimal alignments of the input strings

def traceback():
    s_o = []
    t_o = []
    i = h-1
    j = w-1
    
    while True:
        dir = directions[i][j]
        print(dir)
        if (dir == 0):
            s_o.insert(0, s[i])
            t_o.insert(0, '-')
            i = i-1
        elif (dir == 1):
            s_o.insert(0, '-')
            t_o.insert(0, t[j])
            j = j-1
        else:
            s_o.insert(0, s[i])
            t_o.insert(0, t[j])
            i = i-1
            j = j-1

        if (i == 0 and j == 0):
            break

    return [s_o, t_o]

#--------------------------------------------------------------------------
# Hamming distance is the number of corresponding symbols that differ between s1 and s2
# if used with strings produced by Needleman-Wunsch algorithm, it is the same as edit distance

def compute_hamming_dist(s1, s2):
    diff = 0
    for i in range(len(s1)):
        if (s1[i] != s2[i]):
            diff = diff + 1
    return diff

#--------------------------------------------------------------------------

solution = open('solutions/21-solution.txt', 'w')

records = []
for record in SeqIO.parse("datasets/21-dataset.txt", "fasta"):
    records.append(str(record.seq))

s = '-' + records[0]
t = '-' + records[1]

w = len(t)
h = len(s)

# Needleman-Wunsch algorithm for finding optimal global alignment of two strings
M, directions = initialize()
compute_entries()
[s_o, t_o] = traceback()

solution.write(str(compute_hamming_dist(s_o, t_o)))
solution.close()