"""
5. https://www.codechef.com/problems/CNDY
"""

t_c = int(input())  

for i in range(t_c):
    n_city = int(input())
    arr = input()
    list = arr.split(" ")
    l = []
    for i in range(len(list)):
        count = 1
        for j in range(len(list)):
            if int(list[i])==int(list[j]) and i != j:
                count+=1 
        l.append(count)

    flag = 0
    for j in l:
        if j >= 3:
            flag = 1

    if flag == 0:
        print("YES")
    else:
        print("NO")