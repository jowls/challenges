# 123. Name of challenge
#
# Description

from typing import List

example1_arg1 = [1, 1, 2]
example1_out = 2

example2_arg1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
example2_out = 5


class Solution:
    def solutionFunction(self, prices: List[int]) -> int:
        return 0


print(Solution().solutionFunction(example1_arg1) == example1_out)
print(Solution().solutionFunction(example2_arg1) == example2_out)
