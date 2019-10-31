solution = open('05-solution.txt', 'w')

data = open('datasets/05-dataset.txt')
lines = data.readlines()

for i in range(0,len(lines)):
    if (i%2 == 1):
        solution.write(lines[i])

solution.flush()
solution.close()