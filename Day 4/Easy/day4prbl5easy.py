"""
link: https://leetcode.com/problems/add-binary/
status: submitted

Given two binary strings a and b, return their sum as a binary string.
Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
def addBinary(a, b):
    res = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    while i >= 0 or j >= 0:
        sum = carry
        if i >= 0:
            sum += int(a[i])
            i -= 1
        if j >= 0:
            sum += int(b[j])
            j -= 1
        # right shift
        carry = sum >> 1 
        res.append(str(sum & 1))
    if carry:
        res.append(str(carry))
    return "".join(res[::-1])

print(addBinary("110","101"))