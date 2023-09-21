# 1512. Number of Good Pairs

from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    result += 1
        return result


def test():
    solver = Solution()

    assert solver.numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4
    assert solver.numIdenticalPairs([1, 1, 1, 1]) == 6
    assert solver.numIdenticalPairs([1, 2, 3]) == 0

    print("All tests passed!")
