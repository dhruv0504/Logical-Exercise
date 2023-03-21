"""
6. https://leetcode.com/problems/largest-time-for-given-digits/

"""
from itertools import permutations

def largestTimeFromDigits(A):
    
    arr = list(permutations(sorted(A, reverse=True)))
        
    for h1, h2, m1, m2 in arr:
        if h1 * 10 + h2 < 24 and m1 * 10 + m2 < 60:
            return f'{h1}{h2}:{m1}{m2}'
    return ''

print(largestTimeFromDigits([5,5,5,5]))

# 2nd method (w/o library)

# def largestTimeFromDigits(A):
#     A.sort()
#     for h in range(23, -1, -1):
#         for m in range(59, -1, -1):
#             t = [h//10, h % 10, m // 10, m % 10]
#             ts = sorted(t)
#             if ts == A:
#                 return str(t[0]) + str(t[1]) +':' + str(t[2]) + str(t[3])
#     return ''