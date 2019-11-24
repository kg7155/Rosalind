from Bio import SeqIO
#--------------------------------------------------------------------------------------
# check if all strings contain a substring ss

def is_in_all(ss, strings):
    for s in strings:
        if (ss not in s):
            return False
    return True
#--------------------------------------------------------------------------------------
# find longest common substring among DNA strings

def longest_common_ss():
    shortest_s = min(dna_strings, key=len)
    shortest_s_len = len(shortest_s)
    shortest_idx = dna_strings.index(shortest_s)
    
    max_s = ""
    max_len = 0
    for i in range(shortest_s_len, 0, -1):
        for j in range(shortest_s_len-i+1):
            ss = shortest_s[j:j+i]
            if (is_in_all(ss, dna_strings)):
                max_s = ss
                return max_s
    return max_s
#--------------------------------------------------------------------------------------

solution = open("solutions/43-solution.txt", 'w')

dna_strings = []
for s in SeqIO.parse("datasets/43-dataset.txt", "fasta"):
    dna_strings.append(str(s.seq))

lcs = longest_common_ss()
solution.write(lcs)
solution.close()