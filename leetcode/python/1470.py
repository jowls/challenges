# 1470. Shuffle the Array

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result


def test():
    solver = Solution()

    assert solver.shuffle([2, 5, 1, 3, 4, 7], 3) == [2, 3, 5, 4, 1, 7]
    assert solver.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4) == [1, 4, 2, 3, 3, 2, 4, 1]
    assert solver.shuffle([1, 1, 2, 2], 2) == [1, 2, 1, 2]

    print("All tests passed!")
