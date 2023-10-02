# 228. Summary Ranges

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = prev = None
        result = []
        for n in nums:
            if start is None:
                start = n
            elif abs(n - prev) > 1:
                if prev - start > 0:
                    result.append("{}->{}".format(start, prev))
                else:
                    result.append(str(start))
                start = n
            prev = n

        if start is not None:
            if prev - start > 0:
                result.append("{}->{}".format(start, prev))
            else:
                result.append(str(start))
        print(result)
        return result


def test():
    solver = Solution()

    assert solver.summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert solver.summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
    assert solver.summaryRanges([0]) == ["0"]
    assert solver.summaryRanges([2, -1]) == ["2", "-1"]

    print("All tests passed!")
