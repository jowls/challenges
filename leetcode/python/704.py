# 704. Binary Search

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            num = nums[mid]
            if num == target:
                return mid
            elif num > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1


def test():
    solver = Solution()

    assert solver.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert solver.search([-1, 0, 3, 5, 9, 12], 2) == -1

    print("All tests passed!")
