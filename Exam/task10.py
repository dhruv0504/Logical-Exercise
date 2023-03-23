"""
10. https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145

"""
import itertools

str = "??JJ??"
str_l = [x for x in str]
# print(str_l)
buf = []
# min_cost = 0
x=2
y=-5


for p in itertools.product(['C','J'], repeat=len(str_l)):
    l = list(p)
    # print(l)
    flag = 0
    for i in range(len(str_l)):
        if str_l[i] != l[i] and str_l[i] != '?':
            flag = 1
            break
    if flag == 0:
        buf.append(l)

# print(buf)
for j in range(len(buf)):
    l = buf[j]
    cost = 0
    for i in range(len(l)-1):
        # print(l[i],l[i+1])
        if l[i] == 'J' and l[i+1] == 'C':
            cost += y
            # print(cost)
        if l[i] =='C' and l[i+1] == 'J':
            cost += x
            # print(cost)
    if j == 0:
        min_cost = cost

    if min_cost > cost:
        min_cost = cost
    # print(min_cost)
    
print(min_cost)