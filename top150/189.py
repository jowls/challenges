# 189. Rotate Array

from typing import List

example1_arg1 = [1, 2, 3, 4, 5, 6, 7]
example1_arg2 = 3
example1_out = [5, 6, 7, 1, 2, 3, 4]

example2_arg1 = [-1, -100, 3, 99]
example2_arg2 = 2
example2_out = [3, 99, -1, -100]

example3_arg1 = [1, 2]
example3_arg2 = 3
example3_out = [2, 1]

example4_arg1 = [1, 2]
example4_arg2 = 5
example4_out = [2, 1]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        temp = nums.copy()
        if k > len(nums):
            k = k % len(nums)
        for i in range(len(nums)):
            if (i + k) < len(nums):
                nums[i + k] = temp[i]
            else:
                nums[(i + k) - len(nums)] = temp[i]
        print(nums)


Solution().rotate(example1_arg1, example1_arg2)
Solution().rotate(example2_arg1, example2_arg2)
Solution().rotate(example3_arg1, example3_arg2)
Solution().rotate(example4_arg1, example4_arg2)
