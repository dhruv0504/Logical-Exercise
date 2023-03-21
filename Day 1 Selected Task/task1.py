"""
1. LC(h)
https://leetcode.com/problems/trapping-rain-water/

status: submitted

get reference for logic

"""

heights = [0,1,0,2,1,0,1,3,2,1,2,1]

def rain_trap(arr):
    n = len(arr)

    left = [0] * n
    right = [0] * n
    print(left)
    print(right)
    left[0] = arr[0]
    max_so_far_left = arr[0]


    for i in range(0,n):
        if max_so_far_left < arr[i]:
            max_so_far_left = arr[i]
            left[i] = max_so_far_left
        else:
            left[i] = max_so_far_left
    print(left)


    max_so_far_right = arr[-1]
    
    for i in range(n-1,-1,-1):
        if max_so_far_right < arr[i]:
            max_so_far_right = arr[i]
            right[i] = max_so_far_right
        else:
            right[i] = max_so_far_right
    print(right)

    water = 0
    for i in range(n):
        water += min(left[i],right[i])-arr[i]
    return water

print(rain_trap(heights))