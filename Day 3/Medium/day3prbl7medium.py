"""
link:https://leetcode.com/problems/kth-largest-element-in-an-array/
status: submitted

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
nums = [3,2,3,1,2,4,5,5,6]
k = 4

def k_largest(nums,k):
    for i in range(len(nums)-1):
        for j in range(i,len(nums)):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    return nums[-k]

# second method

# class Solution(object):
#     def findKthLargest(self, nums, k):
#         return sorted(nums)[-k]

print(k_largest(nums,k))