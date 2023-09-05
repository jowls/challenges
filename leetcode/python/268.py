# 268. Missing Number

from typing import List

example1_arg1 = [3, 0, 1]
example1_out = 2

example2_arg1 = [0, 1]
example2_out = 2

example3_arg1 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
example3_out = 8

example4_arg1 = [3, 2, 0]
example4_out = 1


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        idx = 0
        n = len(nums)

        while idx < n:
            if nums[idx] < n and nums[idx] != idx:
                temp = nums[nums[idx]]
                nums[nums[idx]] = nums[idx]
                nums[idx] = temp
            else:
                idx += 1

        for i, a in enumerate(nums):
            if a != i:
                return i

        return len(nums)

    def missingNumberV1(self, nums: List[int]) -> int:
        idx = 0
        n = len(nums)

        while idx < n:
            if nums[idx] == idx or nums[idx] == n:
                idx += 1
                continue
            else:
                temp = nums[nums[idx]]
                nums[nums[idx]] = nums[idx]
                nums[idx] = temp
            if nums[idx] == idx:
                idx += 1
        idx -= 1
        if nums[idx] < n and nums[idx] != idx:
            temp = nums[nums[idx]]
            nums[nums[idx]] = nums[idx]
            nums[idx] = temp

        for i, a in enumerate(nums):
            if a != i:
                return i

        return len(nums)


print(Solution().missingNumber(example1_arg1) == example1_out)
print(Solution().missingNumber(example2_arg1) == example2_out)
print(Solution().missingNumber(example3_arg1) == example3_out)
print(Solution().missingNumber(example4_arg1) == example4_out)
