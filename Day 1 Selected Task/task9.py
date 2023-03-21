"""
9. cfo(m)
https://codeforces.com/problemset/problem/732/A

"""

price = 15
coin = 2

for i in range(1,1000):
    a = (i*10)% price
    if a == 0:
        count = (i*10)/price
        print(count)
        break
    if (((i*10)+coin)%price) == 0:
        count = ((i*10)+coin)/price
        print(count)
        break