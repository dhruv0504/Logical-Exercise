"""
8. https://practice.geeksforgeeks.org/problems/lucky-numbers2911/1?page=1&category[]=Recursion&sortBy=submissions
"""
def isLucky(n): 
    #RETURN True OR False
    for i in range(2,n+1):
        if (n%i) == 0:
            return False
        # return index of number after reductioin
        n = n - (n // i) 
    return True

print(isLucky(19))