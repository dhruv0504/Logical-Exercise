"""
1. https://projecteuler.net/problem=22
"""

with open('C:/Projects/Code Practise/Exam/names.txt') as f:
    lines = f.read()

names = lines.split(',')

f_names = []

for i in range(len(names)):
    n = names[i].strip('\"')
    f_names.append(n)

dict = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26,
}

name = sorted(f_names)
total = 0

for i in range(len(name)):
    l = [x for x in str(name[i])]
    sum = 0
    for j in l:
        sum += dict[j]
    total += (i+1)*sum 
    # print(total)

print(total)