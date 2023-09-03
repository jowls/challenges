# 57. Insert Interval

from typing import List

example1_arg1 = [[1, 3], [6, 9]]
example1_arg2 = [2, 5]
example1_out = [[1, 5], [6, 9]]

example2_arg1 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
example2_arg2 = [4, 8]
example2_out = [[1, 2], [3, 10], [12, 16]]

example3_arg1 = [[1, 5]]
example3_arg2 = [2, 3]
example3_out = [[1, 5]]

example4_arg1 = [[1, 5], [6, 8]]
example4_arg2 = [0, 9]
example4_out = [[0, 9]]


class Solution:
    # O(nlogn)
    def insertV1(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # handle 0-length edge case
        if len(intervals) == 0:
            return [newInterval]

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        # merge intervals
        result = [intervals[0]]

        for lo, hi in intervals[1:]:
            prev_hi = result[-1][1]
            if lo <= prev_hi:
                result[-1][1] = max(hi, prev_hi)
            else:
                result.append([lo, hi])
        print(result)
        return result

    # O(n)
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # handle 0-length edge case
        if len(intervals) == 0:
            return [newInterval]

        result = []
        for idx, a in enumerate(intervals):
            if newInterval[1] < a[0]:
                result.append(newInterval)
                return result + intervals[idx:]
            elif newInterval[0] > a[1]:
                result.append(a)
            else:
                newInterval = [min(a[0], newInterval[0]), max(a[1], newInterval[1])]

        result.append(newInterval)
        return result


print(Solution().insert(example1_arg1, example1_arg2) == example1_out)
print(Solution().insert(example2_arg1, example2_arg2) == example2_out)
print(Solution().insert(example3_arg1, example3_arg2) == example3_out)
print(Solution().insert(example4_arg1, example4_arg2) == example4_out)
