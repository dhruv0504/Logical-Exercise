"""
link: https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

def longestCommonPrefix(strs):
      
    size = len(strs)

    # for null list

    if (size == 0):
        return ""
    
    # for one member list

    if (size == 1):
        return strs[0]

    # for sorting list member in term of length of string

    strs.sort()


    i = 0

    while (i < len(strs[0]) and strs[0][i] == strs[size - 1][i]):
        i += 1
  
    pre = strs[0][0: i]

    len1 = len(pre)
    
    if len1 > 0:
        return pre
    else:
        return ""

  
input = ["fswwer","flower","flow","floght","flwwt"]

print("The longest Common Prefix is :" , longestCommonPrefix(input))
