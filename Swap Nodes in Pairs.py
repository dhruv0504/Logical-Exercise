"""
link: https://leetcode.com/problems/swap-nodes-in-pairs/

Given a list, swap every two adjacent and return it. You must solve the problem without modifying the values in the list (i.e., only themselves may be changed.)

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""

head=[1,2,3,4]

for i in range(0,len(head)-1,2):
  temp=head[i]
  head[i]=head[i+1]
  head[i+1]=temp

print(head)
