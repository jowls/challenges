# 66. Plus One

from typing import List

example1_arg1 = [1, 2, 3]
example1_out = [1, 2, 4]

example2_arg1 = [4, 3, 2, 1]
example2_out = [4, 3, 2, 2]

example3_arg1 = [9]
example3_out = [1, 0]

example4_arg1 = [8, 9, 9, 9]
example4_out = [9, 0, 0, 0]


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = digits
        for i in reversed(range(0, len(result))):
            if result[i] < 9:
                result[i] += 1
                return result
            else:
                result[i] = 0
                if not result[i-1]:
                    result.insert(0, 1)
        return result


print(Solution().plusOne(example1_arg1) == example1_out)
print(Solution().plusOne(example2_arg1) == example2_out)
print(Solution().plusOne(example3_arg1) == example3_out)
print(Solution().plusOne(example4_arg1) == example4_out)
