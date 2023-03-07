"""
link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
status: time exceed error

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums. 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
"""

nums = [4,3,2,7,8,2,3,1]
def findDisappearedNumbers(nums):
    ans = []
    for i in range(1,len(nums)+1):
        if i not in nums:
            ans.append(i)
    return ans

# anothor method

def findDisappearedNumbers(self, nums):        
        return [i for i in range(1, len(nums)+1) if i not in nums]

print(findDisappearedNumbers(nums))