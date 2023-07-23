# 26. Remove Duplicates from Sorted Array
#
# Given an integer array nums sorted in non-decreasing order, remove the
# duplicates in-place such that each unique element appears only once. The
# relative order of the elements should be kept the same. Then return the
# number of unique elements in nums. Consider the number of unique elements of
# nums to be k, to get accepted, you need to do the following things:
#     - Change the array nums such that the first k elements of nums contain
#       the unique elements in the order they were present in nums initially.
#       The remaining elements of nums are not important as well as the size
#       of nums.
#     - Return k.

from typing import List

example1_arg1 = [1, 1, 2]
example1_out = 2

example2_arg1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
example2_out = 5


class Solution:
    def removeDuplicatesV1(self, nums: List[int]) -> int:
        nums_len = len(nums)
        i = 0
        while i < nums_len - 1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
                nums_len -= 1
            else:
                i += 1
        print(nums)
        print(len(nums))
        return len(nums)

    def removeDuplicates(self, nums: List[int]) -> int:
        nums_len = len(nums)
        j = 1
        for i in range(1, nums_len):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        print(nums)
        print(j)
        return j


print(Solution().removeDuplicates(example1_arg1) == example1_out)
print(Solution().removeDuplicates(example2_arg1) == example2_out)
