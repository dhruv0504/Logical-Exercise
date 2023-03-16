"""
link: https://leetcode.com/problems/di-string-match/description/
status: submitted

A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

 

Example 1:

Input: s = "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: s = "III"
Output: [0,1,2,3]
Example 3:

Input: s = "DDI"
Output: [3,2,0,1]
 

Constraints:

1 <= s.length <= 105
s[i] is either 'I' or 'D'.
"""

def diStringMatch(s):
        L,ic,dc=[],0,len(s)
        for i in s:
            if i=='I':
                L.append(ic)
                ic+=1
            else:
                L.append(dc)
                dc-=1
        if s[-1]=='I':L.append(ic)
        else:L.append(dc)
        return L

print(diStringMatch("DDI"))