# 347. Top K Frequent Elements

from typing import List
from collections import defaultdict
import heapq


class Solution:
    # O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        result = []

        for n in nums:
            map[n] += 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for item, freq in map.items():
            bucket[freq].append(item)

        for i in range(len(nums), 0, -1):
            for j in bucket[i]:
                result.append(j)
                if len(result) == k:
                    return result

    # O(nlogk)
    def topKFrequentV2(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        min_heap = []
        for n in nums:
            map[n] += 1

        for m in map:
            if len(min_heap) == k:
                heapq.heappushpop(min_heap, (map[m], m))
            else:
                heapq.heappush(min_heap, (map[m], m))

        return [h[1] for h in min_heap]

    def topKFrequentV1(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for n in nums:
            map[n] += 1

        tuples = list(map.items())
        tuples.sort(key=lambda x: x[1])

        return [t[0] for t in tuples[-k:]]


def test():
    solver = Solution()

    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    output1 = [1, 2]
    assert sorted(solver.topKFrequent(nums1, k1)) == sorted(output1)

    nums2 = [1]
    k2 = 1
    output2 = [1]
    assert sorted(solver.topKFrequent(nums2, k2)) == sorted(output2)

    print("All tests passed!")
