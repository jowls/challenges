# 295. Find Median from Data Stream

from typing import List, Optional
from bisect import insort
import heapq


# two heaps O(log n) solution
class MedianFinder:
    def __init__(self):
        self.small = []  # max heap, needs * -1
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, num * -1)
        if self.large and self.small[0] * -1 > self.large[0]:
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)

        if len(self.small) - len(self.large) > 1:
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)

        if len(self.large) - len(self.small) > 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (self.small[0] * -1 + self.large[0]) / 2.0


# easy O(n) solution
class MedianFinderV1:
    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        insort(self.data, num)

    def findMedian(self) -> float:
        len_data = len(self.data)
        middle = len_data // 2
        if len_data > 0 and len_data % 2 == 0:
            return (self.data[middle - 1] + self.data[middle]) / 2
        else:
            return self.data[middle]


def execute_commands(
    commands: List[str], args: List[List[int]]
) -> List[Optional[float]]:
    results = []
    obj = None

    for cmd, arg in zip(commands, args):
        if cmd == "MedianFinder":
            obj = MedianFinder()
            results.append(None)
        elif cmd == "addNum":
            obj.addNum(arg[0])
            results.append(None)
        elif cmd == "findMedian":
            results.append(obj.findMedian())
    return results


def test():
    commands = [
        "MedianFinder",
        "addNum",
        "addNum",
        "findMedian",
        "addNum",
        "findMedian",
    ]
    args = [[], [1], [2], [], [3], []]
    expected = [None, None, None, 1.5, None, 2.0]
    output = execute_commands(commands, args)
    assert output == expected, f"Expected {expected}, but got {output}"

    print("All tests passed!")
