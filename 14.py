from itertools import permutations 

#--------------------------------------------------------

solution = open('solutions/14-solution.txt', 'w')

with open('datasets/14-dataset.txt') as fp:
    symbols_line = fp.readline().rstrip()
    l = int(fp.readline().rstrip())

symbols = symbols_line.split(' ')
perm = list(permutations(symbols, l))

for symbol in symbols:
    list_symbol = (symbol,) * l
    perm.append(list_symbol)

for p in list(sorted(perm)):
    for i in range(l):
        solution.write(p[i])
    solution.write('\n')

solution.close()