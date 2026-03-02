'''
Would say I kind of did this wrong
two pointer works but its not efficient what so ever

Copy and pasted the better solution on the bottom
Think about it as you just need to see if its the lowest/highest value at any point

case 1: if the price is lower than the loweest we recorded

Then all we do is save the value and set the max to -1

case 2: we find a higher max

Then we actually replace and attempt a comparison

Time complexity: O(n) where n is the length of the prices list, we have to iterate through the list once
Space complexity: O(1) we are only storing a few variables and not using any additional data structures

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0
        
        profit = 0

        l,r = 0,1

        while r < len(prices):

            temp_profit = prices[r] - prices[l]

            if temp_profit < 0:
                l = r

            profit = max(temp_profit, profit)

            r += 1
        
        return profit
    

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 1e5 + 1
        max_price = 0
        for price in prices:
            if price < min_price:
                min_price = price
                max_price = -1
            if price > max_price:
                max_price = price
                max_profit = max(max_profit, max_price - min_price)
        return max_profit if max_profit > 0 else 0