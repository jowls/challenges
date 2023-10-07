# 238. Product of Array Except Self

from typing import List


class Solution:
    # O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = [0] * n, [0] * n
        n = len(nums)

        l[0] = 1
        for i in range(1, n):
            l[i] = nums[i - 1] * l[i - 1]

        # print(l)

        r[n - 1] = 1
        for i in range(n - 2, -1, -1):
            r[i] = nums[i + 1] * r[i + 1]

        # print(r)

        return [l[i] * r[i] for i in range(n)]


def test():
    solver = Solution()

    assert solver.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solver.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert solver.productExceptSelf([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]

    print("All tests passed!")
