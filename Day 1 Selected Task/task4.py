"""
4. gfg(e)
https://practice.geeksforgeeks.org/problems/stock-buy-and-sell-1587115621/1?page=1&curated[]=1&sortBy=submissions

status: submitted

"""
def maxProfit(prices,N):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit = max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        if max_profit > 0:
             return 1
        else: return 0

print(maxProfit([100,180,260,310,40,535,695],52))