"""
1. https://codeforces.com/problemset/problem/1800/D
"""
t_c = int(input("Enter number of test cases:"))

for i in range(t_c):
    len_str = int(input("Enter length of string:"))
    stri = str(input("Enter string:"))
    str_set = []

    for i in range(len_str-1):
        str_buff= ""
        for j in range(len_str):          
            if j != i and j != i+1:
                str_buff += stri[j]
        str_set.append(str_buff)

    print(len(set(str_set)))    
