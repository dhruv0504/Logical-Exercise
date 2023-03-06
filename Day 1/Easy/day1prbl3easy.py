"""
link: https://leetcode.com/problems/two-sum/description/
ans-link: https://colab.research.google.com/drive/1yPBeEiZHVcuRDG3lxSU1FYn9_irVjUYA

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists."""

class Solution(object):
    def twoSum(self, nums, target):
        buff=[]
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                sum = nums[i] + nums[j]
                if sum == target and i != j:
                    buff.append(i)
                    buff.append(j)
        return buff[:2]

# nums = [2,7,11,7,15]
# target = 14

nums = [55, 20, 35, 31, 89, 81, 85, 100, 22, 28, 82, 12, 61, 69, 98, 99, 23, 48, 77, 70, 65, 95, 52, 77, 14, 34, 80, 66, 47, 79, 44, 10, 63, 65, 68, 32, 85, 73, 38, 83, 79, 34, 33, 17, 66, 40, 23, 10, 47, 60, 79, 67, 58, 33, 24, 35, 10, 62, 50, 35, 16, 17, 39, 37, 72, 38, 37, 56, 41, 27, 53, 83, 15, 38, 26, 41, 17, 66, 73, 53, 74, 26, 62, 48, 56, 13, 73, 22, 48, 35, 28, 14, 66, 24, 18, 41, 15, 90, 16, 63]
target = 100

a = Solution()
indices = a.twoSum(nums,target)
print(indices)
print(nums[indices[0]])
print(nums[indices[1]])




