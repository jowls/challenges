# 167. Two Sum II - Input Array Is Sorted

from typing import List

example1_arg1 = [2, 7, 11, 15]
example1_arg2 = 9
example1_out = [1, 2]

example2_arg1 = [2, 3, 4]
example2_arg2 = 6
example2_out = [1, 3]

example3_arg1 = [-1, 0]
example3_arg2 = -1
example3_out = [1, 2]


class Solution:
    def twoSumV1(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i, n in enumerate(numbers):
            rem = target - n
            if rem in dict:
                return [dict[rem] + 1, i + 1]
            else:
                dict[n] = i

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        while low < high:
            if numbers[low] + numbers[high] > target:
                high -= 1
            elif numbers[low] + numbers[high] < target:
                low += 1
            else:
                return [low + 1, high + 1]


print(Solution().twoSum(example1_arg1, example1_arg2) == example1_out)
print(Solution().twoSum(example2_arg1, example2_arg2) == example2_out)
print(Solution().twoSum(example3_arg1, example3_arg2) == example3_out)
