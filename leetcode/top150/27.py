# 27. Remove Element
#
# Given an integer array nums and an integer val, remove all occurrences of
# val in nums in-place. The order of the elements may be changed. Then return
# the number of elements in nums which are not equal to val. Consider the
# number of elements in nums which are not equal to val be k, to get accepted,
# you need to do the following things:
#     - Change the array nums such that the first k elements of nums contain
#       the elements which are not equal to val. The remaining elements of
#       nums are not important as well as the size of nums.
#     - Return k.

from typing import List

example1_arg1 = [3, 2, 2, 3]
example1_arg2 = 3
example1_out = 2

example2_arg1 = [0, 1, 2, 2, 3, 0, 4, 2]
example2_arg2 = 2
example2_out = 5


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_len = len(nums)
        i = 0
        while i < nums_len:
            if nums[i] == val:
                nums.pop(i)
                nums_len -= 1
            else:
                i += 1
        print(nums)
        print(len(nums))
        return len(nums)


print(Solution().removeElement(example1_arg1, example1_arg2) == example1_out)
print(Solution().removeElement(example2_arg1, example2_arg2) == example2_out)
