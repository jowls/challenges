# 1929. Concatenation of Array
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


def test():
    solver = Solution()

    assert solver.getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert solver.getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]

    print("All tests passed!")
