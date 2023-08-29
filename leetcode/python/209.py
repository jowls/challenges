# 209. Minimum Size Subarray Sum

from typing import List

example1_arg1 = 7
example1_arg2 = [2, 3, 1, 2, 4, 3]
example1_out = 2

example2_arg1 = 4
example2_arg2 = [1, 4, 4]
example2_out = 1

example3_arg1 = 11
example3_arg2 = [1, 1, 1, 1, 1, 1, 1, 1]
example3_out = 0

example4_arg1 = 15
example4_arg2 = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
example4_out = 2


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = min_sub = total = 0

        # expand the sliding window
        while r < len(nums):
            total += nums[r]
            r += 1

            # contract the sliding window
            while total >= target and l <= r:
                total -= nums[l]
                l += 1
                if r - l + 1 < min_sub or min_sub == 0:
                    min_sub = r - l + 1

        return min_sub


print(Solution().minSubArrayLen(example1_arg1, example1_arg2) == example1_out)
print(Solution().minSubArrayLen(example2_arg1, example2_arg2) == example2_out)
print(Solution().minSubArrayLen(example3_arg1, example3_arg2) == example3_out)
print(Solution().minSubArrayLen(example4_arg1, example4_arg2) == example4_out)
