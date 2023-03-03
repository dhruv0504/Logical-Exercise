"""
link: https://leetcode.com/problems/number-of-digit-one/


Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example 1:

Input: n = 13
Output: 6
Example 2:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 109
"""

n=0
count = 0

for j in range(n+1):
  list_of_digits = [int(i) for i in str(j)]
  for k in range(len(list_of_digits)):
    if list_of_digits[k] == 1:
      count+=1

print(count)
