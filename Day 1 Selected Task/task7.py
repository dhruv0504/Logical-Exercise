"""
7. cfo(e)
https://codeforces.com/problemset/problem/705/A

status: submit doubt
"""

def strings(n):
    li = ["I hate " , "I Love " , "that " , "it"]
    stri = ""
    for i in range(n):
        if i%2==0:
            stri += li[0]
            if i == n-1:
                stri += li[3]
            else:
                stri += li[2]
        else:
            stri += li[1]
            if i == n-1:
                stri += li[3]
            else:
                stri += li[2]
    return stri

print(strings(3))