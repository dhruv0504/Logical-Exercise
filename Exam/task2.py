"""
2. https://codeforces.com/problemset/problem/1792/B
"""

t_c = int(input())

for i in range(t_c):
    t = input()
    t_l = t.split(" ")        

    count = 0

    if int(t_l[0]) == 0:
        print(1)
    else:
        count = int(t_l[0]) + min(int(t_l[1]),int(t_l[2]))*2 + min(abs(int(t_l[1])-int(t_l[2]))+int(t_l[3]),int(t_l[0])+1)
        print(count)
