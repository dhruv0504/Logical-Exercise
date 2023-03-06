"""
link: https://leetcode.com/problems/basic-calculator/
status: submitted

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""
def calculate(s):
        stack = []
        p = 0
        sign = 1
        total = 0
        while p < len(s):
            char = s[p]
            if char.isdigit():
                num = 0
                while p < len(s) and s[p].isdigit():
                    num = num*10 + int(s[p])
                    p += 1
                p -= 1
                num *= sign
                total += num
                sign = 1
            elif char == '(':
                stack.append(total)
                stack.append(sign)
                total, sign = 0, 1
            elif char == ')':
                total *= stack.pop()
                total += stack.pop()
            elif char == '-':
                sign = -1
            p += 1
        return total

s = " 2-1 + 2 "
print(calculate(s))