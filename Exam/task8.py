"""
8. https://leetcode.com/problems/apply-discount-every-n-orders/
"""

class Cashier:

    def __init__(self, n, discount, products, prices):
        self.prices = {products[i]:prices[i] for i in range(len(products))}
        self.n = n
        self.discount = discount
        self.cus = 0
        
    def getBill(self, product, amount):
        total_bill = 0
        
        for i in range(len(product)):
            total_bill += self.prices[product[i]] * amount[i]
        
        self.cus += 1
        if self.cus % self.n == 0:
            return total_bill * (100 - self.discount )/100
        
        return total_bill
    

