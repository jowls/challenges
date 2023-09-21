# 1431. Kids With the Greatest Number of Candies

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        most = max(candies)
        return [x + extraCandies >= most for x in candies]


def test():
    solver = Solution()

    assert solver.kidsWithCandies([2, 3, 5, 1, 3], 3) == [True, True, True, False, True]
    # fmt: off
    assert solver.kidsWithCandies([4,2,1,1,2], 1) \
                               == [True,False,False,False,False]
    # fmt: on
    assert solver.kidsWithCandies([12, 1, 12], 10) == [True, False, True]

    print("All tests passed!")
