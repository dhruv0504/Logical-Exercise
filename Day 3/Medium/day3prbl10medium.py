"""
link: https://leetcode.com/problems/sort-list/
status: submitted

Given the head of a linked list, return the list after sorting it in ascending order.
Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
"""
def sortList(self, head):
        if not head: return
        
        ## iterate the list
        node, l = head, [[head.val, head]]
        while node.next:
            node = node.next
            l.append([node.val, node])
            
        l.sort(key=lambda x:x[0])
		
		## reconstruct the list
        node = head = l[0][1]
        for k,v in l[1:]:
            node.next = v
            node = node.next
        node.next = None
        
        return head

print(sortlist([4,2,1,3]))