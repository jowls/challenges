# 121. Best Time to Buy and Sell Stock
#
# You are given an array prices where prices[i] is the price of a given stock
# on the ith day. You want to maximize your profit by choosing a single day to
# buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you
# cannot achieve any profit, return 0.

from typing import List

example1_arg1 = [7, 1, 5, 3, 6, 4]
example1_out = 5

example2_arg1 = [7, 6, 4, 3, 1]
example2_out = 0


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            todays_price = prices[i]
            if todays_price < min_price:
                min_price = todays_price
            else:
                profit = todays_price - min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit


print(Solution().maxProfit(example1_arg1) == example1_out)
print(Solution().maxProfit(example2_arg1) == example2_out)
