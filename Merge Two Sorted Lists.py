""""
link: https://leetcode.com/problems/merge-two-sorted-lists/ 

You are given the heads of two sorted lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
Both list1 and list2 are sorted in non-decreasing order.
"""




class Solution(object):
    def mergeTwoLists(self, list1, list2):
        list = list1 + list2
        n = len(list)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if list[j] > list[j + 1]:
                   list[j], list[j + 1] = list[j + 1], list[j]
        return list

li1 = [1,2,4,4,1,2,1]
li2 = [1,3,4,1,54,4,2]

ans = Solution()

fa = ans.mergeTwoLists(li1,li2)
print(fa)
