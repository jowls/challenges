# 448. Find All Numbers Disappeared in an Array

from typing import List

example1_arg1 = [4, 3, 2, 7, 8, 2, 3, 1]
example1_out = [5, 6]

example2_arg1 = [1, 1]
example2_out = [2]


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        idx = 0
        while idx < len(nums):
            correct_idx = nums[idx] - 1  # find correct position for current num

            # swap current num to correct position if not already there
            if nums[correct_idx] != nums[idx]:
                nums[idx], nums[correct_idx] = nums[correct_idx], nums[idx]
            else:
                idx += 1

        # correct_idx of nums not in their expected positions are the missing ones
        result = [i + 1 for i, num in enumerate(nums) if num != i + 1]

        return result

    def findDisappearedNumbersV1(self, nums: List[int]) -> List[int]:
        idx = 0
        n = len(nums)
        result = []

        while idx < n:
            if nums[nums[idx] - 1] != nums[idx]:  # val at idx not previously corrected
                temp = nums[nums[idx] - 1]
                nums[nums[idx] - 1] = nums[idx]
                nums[idx] = temp
            else:
                idx += 1

        for i, a in enumerate(nums):
            if a != i + 1:
                result.append(i + 1)

        return result


print(Solution().findDisappearedNumbers(example1_arg1) == example1_out)
print(Solution().findDisappearedNumbers(example2_arg1) == example2_out)
