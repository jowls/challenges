# 88. Merge Sorted Array
#
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing
# order, and two integers m and n, representing the number of elements in nums1
# and nums2 respectively. Merge nums1 and nums2 into a single array sorted in
# non-decreasing order.
# The final sorted array should not be returned by the function, but instead be
# stored inside the array nums1. To accommodate this, nums1 has a length of
# m + n, where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a
# length of n.

from typing import List

example1_arg1 = [1, 2, 3, 0, 0, 0]
example1_arg2 = 3
example1_arg3 = [2, 5, 6]
example1_arg4 = 3
example1_out = [1, 2, 2, 3, 5, 6]

example2_arg1 = [1]
example2_arg2 = 1
example2_arg3 = []
example2_arg4 = 0
example2_out = [1]

example3_arg1 = [0]
example3_arg2 = 0
example3_arg3 = [1]
example3_arg4 = 1
example3_out = [1]


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        for i in range(m, m+n):
            nums1[i] = nums2[i-m]
        nums1.sort()


Solution().merge(example1_arg1, example1_arg2, example1_arg3, example1_arg4)
print(example1_arg1 == example1_out)
Solution().merge(example2_arg1, example2_arg2, example2_arg3, example2_arg4)
print(example2_arg1 == example2_out)
Solution().merge(example3_arg1, example3_arg2, example3_arg3, example3_arg4)
print(example3_arg1 == example3_out)
