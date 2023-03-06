"""
LINK: https://leetcode.com/problems/counting-bits/

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
"""

def to_binary(num):
    list=[]
    while(num >= 1):
        a = num % 2
        num = num//2  
        if a == 1:
            list.append(a)
    return list

num = 5

count_list = []


for i in range(0,num+1):
    count = 0
    ans = to_binary(i)
    for i in ans:
        if i == 1:
            count+=1
    count_list.append(count) 

print(count_list)