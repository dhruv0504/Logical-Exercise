"""
link: https://leetcode.com/problems/median-of-two-sorted-arrays/


Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

list1 = [1,3,11,34,21,21,24,56,67]
list2 = [2,4,3,12,5,6,87]

m_list = list1 + list2

s_list = sorted(m_list)
print(s_list)
print(len(s_list))
print(len(s_list) // 2)
length = len(s_list)
h_len = length//2

if length % 2 ==0:
  median = (s_list[h_len-1] + s_list[h_len])/2
else:
  median = s_list[h_len] 

print('%.5f' % median)
