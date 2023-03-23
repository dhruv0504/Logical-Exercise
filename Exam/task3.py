"""
3. https://codeforces.com/problemset/problem/1765/E

"""

t_c = 1

for i in range(t_c):
    n = 9999997
    # 1 gc = 25 sc (SELL GC)
    a = 25   
    # 30 sc = 1 gc (BUY GC)
    b = 50

    if a < b:
        ans  = int(n / a) + (n % a > 0)
        print(ans) 
    else:
        print(1)
        