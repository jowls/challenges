# 1. Two Sum

from typing import List

example1_arg1 = [2, 7, 11, 15]
example1_arg2 = 9
example1_out = [0, 1]

example2_arg1 = [3, 2, 4]
example2_arg2 = 6
example2_out = [1, 2]

example3_arg1 = [3, 3]
example3_arg2 = 6
example3_out = [0, 1]


class Solution:
    def twoSumV1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_hash = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in temp_hash:
                return [temp_hash[remainder], i]
            temp_hash[nums[i]] = i
        return []


print(Solution().twoSumV1(example1_arg1, example1_arg2) == example1_out)
print(Solution().twoSumV1(example2_arg1, example2_arg2) == example2_out)
print(Solution().twoSumV1(example3_arg1, example3_arg2) == example3_out)

print(Solution().twoSum(example1_arg1, example1_arg2) == example1_out)
print(Solution().twoSum(example2_arg1, example2_arg2) == example2_out)
print(Solution().twoSum(example3_arg1, example3_arg2) == example3_out)
