# 442. Find All Duplicates in an Array

from typing import List

example1_arg1 = [4, 3, 2, 7, 8, 2, 3, 1]
example1_out = [2, 3]

example2_arg1 = [1, 1, 2]
example2_out = [1]

example3_arg1 = [1]
example3_out = []


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        idx = 0
        while idx < len(nums):
            correct_idx = nums[idx] - 1  # find correct position for current num
            # swap current num to correct position if not already there
            if nums[idx] != nums[correct_idx]:
                nums[idx], nums[correct_idx] = nums[correct_idx], nums[idx]
            else:
                idx += 1

        dups = [num for i, num in enumerate(nums) if num != i + 1]
        return dups

    from typing import List

    def findDuplicatesV1(self, nums: List[int]) -> List[int]:
        result = set()
        idx = 0
        n = len(nums)

        while idx < n:
            if nums[nums[idx] - 1] == nums[idx] and nums[idx] != idx + 1:
                result.add(nums[idx])
                idx += 1
            elif nums[nums[idx] - 1] != idx + 1:
                temp = nums[nums[idx] - 1]
                nums[nums[idx] - 1] = nums[idx]
                nums[idx] = temp
            else:
                idx += 1

        return list(result)

    from typing import List


print(Solution().findDuplicates(example1_arg1) == example1_out)
print(Solution().findDuplicates(example2_arg1) == example2_out)
print(Solution().findDuplicates(example3_arg1) == example3_out)
