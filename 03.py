with open('datasets/03-dataset.txt') as fp:
    myString = fp.readline()
    numLine = fp.readline()

a = int(numLine.split(' ')[0])
b = int(numLine.split(' ')[1])
c = int(numLine.split(' ')[2])
d = int(numLine.split(' ')[3])

print(myString[a:b+1] + ' ' + myString[c:d+1])