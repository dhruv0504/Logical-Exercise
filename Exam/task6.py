"""
6. https://practice.geeksforgeeks.org/problems/product-array-puzzle4525/1?page=2&company[]=Morgan%20Stanley&company[]=Intuit&company[]=Directi&sortBy=submissions

"""
nums = [10,3,5,6,2]
li = []
for i in range(len(nums)):
    mul = 1
    for j in range(len(nums)):
        if i != j:
            mul *= nums[j]
    li.append(mul)
print(li)   