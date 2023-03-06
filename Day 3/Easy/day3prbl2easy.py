"""
link: https://leetcode.com/problems/move-zeroes/
status: submitted

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""
def reorder(A):
 
    # `k` stores the index of the next available position
    k = 0
 
    # do for each element
    for i in A:
        # if the current element is non-zero, put the element at the
        # next free position in the list
        if i:
            A[k] = i
            k = k + 1
 
    # move all 0's to the end of the list (remaining indices)
    for i in range(k, len(A)):
        A[i] = 0
    print(A)
    
list = [1,0,2,3,50,0,1,0]
print(reorder(list))