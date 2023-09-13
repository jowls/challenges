# 480. Sliding Window Median

from typing import List
import heapq


class Solution:
    # O(n * log k)
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def rebalance():
            # if the balance is negative, transfer a number from the large to small heap
            if balance < 0:
                val = heapq.heappop(large)
                heapq.heappush(small, -val)

            # if the balance is positive, transfer a number from the small to large heap.
            elif balance > 0:
                val = -heapq.heappop(small)
                heapq.heappush(large, val)

            # handle lazy deletions if they're at the root of our heaps
            while small and -small[0] in to_del:
                val = -heapq.heappop(small)
                to_del[val] -= 1
                if to_del[val] == 0:
                    del to_del[val]

            while large and large[0] in to_del:
                val = heapq.heappop(large)
                to_del[val] -= 1
                if to_del[val] == 0:
                    del to_del[val]

        def median():
            # k is even
            if k % 2 == 0:
                return (-small[0] + large[0]) / 2
            # k is odd
            else:
                return -small[0]

        small, large = [], []  # small heap values must be negated
        to_del = {}  # track lazy deletes
        result = []
        n = len(nums)

        # init the window to small (max) heap
        for i in range(k):
            heapq.heappush(small, -nums[i])

        # init rebalance
        for _ in range(k // 2):
            val = -heapq.heappop(small)
            heapq.heappush(large, val)

        for i in range(0, n - k + 1):
            result.append(float(median()))

            # avoid an index error in the last iteration
            if i == n - k:
                break

            # lazy delete nums[i] from heaps
            val = nums[i]
            to_del[val] = to_del.get(val, 0) + 1

            if nums[i] <= -small[0]:
                balance = -1
            else:
                balance = 1

            # add next value to correct heap and adjust balance num accordingly:
            #
            # e.g. if balance is negative, we have deleted the item sliding out of the
            # window from the small heap. if the value sliding into the window should
            # be added to the small heap, then balance is restored (to 0). otherwise
            # it becomes -2 and will be handled in the rebalance() helper function

            if not small or nums[k + i] <= -small[0]:
                balance += 1
                heapq.heappush(small, -nums[k + i])
            else:
                balance -= 1
                heapq.heappush(large, nums[k + i])

            rebalance()
        # print(result)
        return result


def test():
    solver = Solution()

    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    assert solver.medianSlidingWindow(nums, k) == [
        1.00000,
        -1.00000,
        -1.00000,
        3.00000,
        5.00000,
        6.00000,
    ]

    nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
    k = 3
    assert solver.medianSlidingWindow(nums, k) == [
        2.00000,
        3.00000,
        3.00000,
        3.00000,
        2.00000,
        3.00000,
        2.00000,
    ]

    nums = [9, 7, 0, 3, 9, 8, 6, 5, 7, 6]
    k = 2
    assert solver.medianSlidingWindow(nums, k) == [
        8.00000,
        3.50000,
        1.50000,
        6.00000,
        8.50000,
        7.00000,
        5.50000,
        6.00000,
        6.50000,
    ]

    print("All tests passed!")
