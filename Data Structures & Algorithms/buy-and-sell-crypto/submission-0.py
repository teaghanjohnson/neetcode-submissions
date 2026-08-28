class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, len(prices)- 1
        profit = 0
        while l < len(prices)- 1:
            while r > l:
                new_profit = prices[r] - prices[l]
                if new_profit > profit:
                    profit = new_profit
                else:
                    r -= 1
            r = len(prices)-1
            l += 1
        
        return profit

        