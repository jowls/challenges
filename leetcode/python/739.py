# 739. Daily Temperatures

from typing import List

example1_arg1 = [73, 74, 75, 71, 69, 72, 76, 73]
example1_out = [1, 1, 4, 2, 1, 1, 0, 0]

example2_arg1 = [30, 40, 50, 60]
example2_out = [1, 1, 1, 0]

example3_arg1 = [30, 60, 90]
example3_out = [1, 1, 0]


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # init empty result array
        result = [0] * len(temperatures)
        # stack is monotonic decreasing(by temp) tuples representing: temp, and its index within temperatures array
        stack = []

        for i, a in enumerate(temperatures):
            while stack and a > stack[-1][0]:
                temp, temp_idx = stack.pop()
                result[temp_idx] = i - temp_idx
            stack.append((a, i))
        print(result)
        return result


def test():
    solver = Solution()
    # fmt:off
    assert (
        solver.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
                              == [1, 1, 4, 2, 1, 1, 0, 0]
    )
    # fmt:on
    assert solver.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert solver.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
    print("All tests passed!")
