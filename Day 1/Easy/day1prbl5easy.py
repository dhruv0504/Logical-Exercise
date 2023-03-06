"""
link:https://leetcode.com/problems/single-number/
ans-link:https://colab.research.google.com/drive/1JeqF4X156Li08KmQyeDtMo3dCqf6Axc8

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""

nums = [4,1,2,1,2,9]


                
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        
        if nums[i] == nums[j]:
            count= count + 1
    
    
    if count == 1:
        print(nums[i])