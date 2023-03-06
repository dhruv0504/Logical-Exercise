"""
link:https://leetcode.com/problems/valid-palindrome/
ans-link: https://colab.research.google.com/drive/1EbAtoeuB6MQ-bGFsB2_TABOcOs6jDOtT

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

s = "race a car"

alnum_s = [t.lower() for t in s if t.isalnum()]

alnum_s_rev = alnum_s[::-1]

if alnum_s_rev == alnum_s:
    print("True")
else:
    print("False")