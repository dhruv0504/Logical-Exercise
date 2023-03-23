"""
7. https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1?page=1&company[]=Flipkart&curated[]=1&sortBy=submissions

"""

arr = [10, 10, 10]
count = 0 
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if arr[i] > arr[j]:
            count += 1
print(count)