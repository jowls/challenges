# 122. Best Time to Buy and Sell Stock II

from typing import List


class Solution:
    # O(n)
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) == 1:
            return profit
        holding = False
        buy_price = 0
        for i in range(1, len(prices)):
            prev = prices[i - 1]
            cur = prices[i]
            if not holding and prev < cur:
                buy_price = prev
                holding = True
            elif holding and prev > buy_price and prev > cur:
                profit += prev - buy_price
                holding = False
        if holding:
            profit += cur - buy_price
        return profit


def test():
    solver = Solution()

    assert solver.maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert solver.maxProfit([1, 2, 3, 4, 5]) == 4
    assert solver.maxProfit([7, 6, 4, 3, 1]) == 0

    print("All tests passed!")
