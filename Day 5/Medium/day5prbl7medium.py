"""
link: https://leetcode.com/problems/powx-n/
status: submitted

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
-104 <= xn <= 104


"""
# method 1

# def myPow(x,n):
#     ans = 1
#     if n > 0:
#         while(n>0):
#             ans *= x
#             n -= 1  
#     elif n < 0:
#         while(n<0):
#             ans /= x
#             n += 1
#     else:
#         ans = 1
    
#     return "{0:.5f}".format(ans)    

# print(myPow(2,-2))

# method 2 

def myPow(x, n):
        return x**n

print(myPow(2,-2))
