# 56. Merge Intervals

from typing import List

example1_arg1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
example1_out = [[1, 6], [8, 10], [15, 18]]

example2_arg1 = [[1, 4], [4, 5]]
example2_out = [[1, 5]]


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn)
        intervals.sort(key=lambda i: i[0])
        results = [intervals[0]]
        for lo, hi in intervals[1:]:
            prev_hi = results[-1][1]
            if prev_hi >= lo:
                results[-1][1] = max(hi, prev_hi)
            else:
                results.append([lo, hi])
        return results


print(Solution().merge(example1_arg1) == example1_out)
print(Solution().merge(example2_arg1) == example2_out)
