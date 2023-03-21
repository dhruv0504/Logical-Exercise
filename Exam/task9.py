"""
9. https://leetcode.com/problems/apply-discount-every-n-orders/
"""

def canPlaceFlowers(flowerbed, n):
    for i in range(len(flowerbed)):
        if i == 0:
            if flowerbed[i] == 0 and len(flowerbed) == 1:
                n-= 1
            elif flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1

        elif i == len(flowerbed)-1:
            if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n-=1
        else:
            if flowerbed[i-1] != 1 and flowerbed[i+1] != 1 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n-=1

    if n <= 0:
        return True 
    else:
        return False
    
print(canPlaceFlowers([1,0,0,0,1],2))