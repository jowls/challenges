# 274. H-Index

from typing import List


class Solution:
    # O(n)
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        papers = [0] * (n + 1)

        # count the papers
        for i, cit in enumerate(citations):
            papers[min(n, cit)] += 1

        # find the h-index
        h = n
        s = papers[h]
        while h > s:
            h -= 1
            s += papers[h]
        return h

    # O(n logn)
    def hIndexV1(self, citations: List[int]) -> int:
        citations.sort()
        h = 0
        for i, paper in enumerate(reversed(citations)):
            if paper >= i + 1:
                h = min(i + 1, paper)

        return h


def test():
    solver = Solution()

    assert solver.hIndex([3, 0, 6, 1, 5]) == 3
    assert solver.hIndex([1, 3, 1]) == 1

    print("All tests passed!")


def testV1():
    solver = Solution()

    assert solver.hIndexV1([3, 0, 6, 1, 5]) == 3
    assert solver.hIndexV1([1, 3, 1]) == 1

    print("All tests passed!")
