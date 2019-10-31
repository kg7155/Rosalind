from collections import Counter

solution = open('solutions/07-solution.txt', 'w')

with open('datasets/07-dataset.txt') as fp:
    myString = fp.readline().rstrip()

nucleus_dict = Counter(myString)

for k, v in sorted(nucleus_dict.items()):
    solution.write(str(v) + ' ')

solution.close()