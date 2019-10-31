from collections import Counter

with open('datasets/06-dataset.txt') as fp:
    myString = fp.readline().rstrip()

word_dict = Counter(myString.split(' '))

for k, v in word_dict.items():
    print(k, ' ', v)