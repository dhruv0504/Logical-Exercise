"""
link: https://leetcode.com/problems/search-insert-position/
ans-link: https://colab.research.google.com/drive/1d7O8SItnbkU8VpweAVG_4__nFK2JgW90

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

class Solution():
    
    def searchInsert(self, nums, target):
        try:
            return nums.index(target)
        except:
            for i in range(len(nums)):
                if nums[i] > target:
                    return i  

nums=[1,3,5,6]
target = 7

ans = Solution()
print(ans.searchInsert(nums,target))