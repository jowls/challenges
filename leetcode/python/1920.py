# 1920. Build Array from Permutation

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]


def test():
    solver = Solution()

    assert solver.buildArray([0, 2, 1, 5, 3, 4]) == [0, 1, 2, 4, 5, 3]
    assert solver.buildArray([5, 0, 1, 2, 3, 4]) == [4, 5, 0, 1, 2, 3]

    print("All tests passed!")
