# 1672. Richest Customer Wealth

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(a) for a in accounts)


def test():
    solver = Solution()

    assert solver.maximumWealth([[1, 2, 3], [3, 2, 1]]) == 6
    assert solver.maximumWealth([[1, 5], [7, 3], [3, 5]]) == 10
    assert solver.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17

    print("All tests passed!")
