"""
link: https://leetcode.com/problems/longest-consecutive-sequence/
status: submitted

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

nums = [100,4,200,1,3,2]

def longestConsecutive(nums):
    max_len = 0
    num_set = set(nums)
    for num in nums:
        curr_num = num
        curr_len = 1
        while curr_num + 1 in num_set:
            curr_num += 1
            curr_len += 1
        max_len = max(max_len, curr_len)
    return max_len

print(longestConsecutive(nums))