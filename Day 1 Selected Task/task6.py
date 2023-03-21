"""
6. cfo(e)
https://codeforces.com/problemset/problem/617/A

status: submit doubt
"""
def steps(dist):
    steps = [5,4,3,2,1]
    count = 0
    for i in range(len(steps)):
        if dist >= steps[i]:
            count += dist//steps[i]
            dist = dist % steps[i]  
    return count

