from Bio import SeqIO
#--------------------------------------------------------------------------------------
# compute transition/transversion ratio
# transition: A <--> G or C <--> T
# transversion: A <--> C or T ... G <--> T or C ... C <--> G or A ... T <--> G or A

def compute_tt_ratio():
    s1 = str(dna_strings[0])
    s2 = str(dna_strings[1])
    transitions = 0
    transversions = 0
    for i in range(len(s1)):
        pyr_1 = (s1[i] == 'T' or s1[i] == 'C')
        pyr_2 = (s2[i] == 'T' or s2[i] == 'C')
        if (pyr_1 == pyr_2 and s1[i] != s2[i]):
            transitions += 1
        elif (pyr_1 != pyr_2):
            transversions += 1
    return transitions/transversions
#--------------------------------------------------------------------------------------

solution = open("solutions/39-solution.txt", 'w')

dna_strings = []
for s in SeqIO.parse("datasets/39-dataset.txt", "fasta"):
    dna_strings.append(s.seq)

tt_ratio = compute_tt_ratio()
solution.write(str(tt_ratio))
solution.close()