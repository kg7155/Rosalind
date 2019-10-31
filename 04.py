with open('datasets/04-dataset.txt') as fp:
    numLine = fp.readline()

a = int(numLine.split(' ')[0])
b = int(numLine.split(' ')[1])

sum = 0
for i in range(a, b+1):
    if (i%2 == 1):
        sum = sum + i

print(sum)