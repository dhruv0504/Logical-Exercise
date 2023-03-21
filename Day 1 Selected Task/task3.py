"""
3. GFG(e)
https://practice.geeksforgeeks.org/problems/equilibrium-point-1587115620/1?page=1&curated[]=1&sortBy=submissions

status: time exceed error

"""

A = [1,3,5,2,2]

def equilibriumPoint(A):
    for i in range(len(A)):
        sum_left = 0
        sum_right = 0
        for j in range(0,i):
            sum_left += A[j] 
        for k in range(i+1,len(A)):
            sum_right += A[k]
        if sum_left == sum_right:
            return i+1
            break
    return -1
        
print(equilibriumPoint(A))