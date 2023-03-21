"""
4. https://codeforces.com/problemset/problem/1793/A
"""

d1 = 10
d2 = 90
req = 10
prom = 8    
price = 0

while(req>0):

    if req >= prom + 1:
        price += d1*prom
        # print(price)
        req -= prom + 1
        # print(req)
    else:
        if d1 < d2:
            price += d1
            # print(price)
            req -= 1
            # print(req)
        else:
            price += d2
            # print(price)
            req -= 1  
            # print(req)  

print(price)
