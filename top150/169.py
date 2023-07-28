# 169. Majority Element
#
# Given an array nums of size n, return the majority element. The majority
# element is the element that appears more than ⌊n / 2⌋ times. You may assume
# that the majority element always exists in the array.

from typing import List

example1_arg1 = [3, 2, 3]
example1_out = 3

example2_arg1 = [2, 2, 1, 1, 1, 2, 2]
example2_out = 2


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        candidate_number = None
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != candidate_number:
                candidate_number = nums[i]
                count = 1
            else:
                count += 1
            if count > n/2:
                return nums[i]


print(Solution().majorityElement(example1_arg1) == example1_out)
print(Solution().majorityElement(example2_arg1) == example2_out)
