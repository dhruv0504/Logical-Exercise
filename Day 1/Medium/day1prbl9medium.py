"""
link: https://leetcode.com/problems/swap-nodes-in-pairs/
ans-link: https://colab.research.google.com/drive/18NFSDilkt3bxcQiBK1fW6Dfn2KvL1pL-

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

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