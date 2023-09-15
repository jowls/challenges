# 78. Subsets

from typing import List


class Solution:
    # O(n * 2^n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(i: int, subset: List[int]):
            if i >= len(nums):
                result.append(subset[:])
                return

            # two choices, do both:
            # 1. do not add nums[i] to the subset
            backtrack(i + 1, subset[:])

            # 2. add nums[i] to the subset
            subset.append(nums[i])
            backtrack(i + 1, subset[:])

        backtrack(0, [])
        return result


def test():
    solver = Solution()

    nums = [1, 2, 3]
    expected_output = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    result = solver.subsets(nums)
    assert sorted(map(sorted, result)) == sorted(map(sorted, expected_output))

    nums = [0]
    expected_output = [[], [0]]
    result = solver.subsets(nums)
    assert sorted(map(sorted, result)) == sorted(map(sorted, expected_output))

    print("All tests passed!")
