# 215. Kth Largest Element in an Array

from typing import List
import random


class Solution:
    # O(n) avg, O(n^2) worst
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        right = n - 1
        left = 0
        target_idx = n - k

        def quickSelect(left: int, right: int) -> int:
            l = left  # left pointer
            m = left  # middle pointer
            r = right  # right pointer
            pivot_idx = random.randint(left, right)  # random pivot index
            pivot = nums[pivot_idx]

            # scan all nums with m
            while m <= r:
                # if less than pivot move nums[m] to the left side
                if nums[m] < pivot:
                    nums[m], nums[l] = nums[l], nums[m]
                    l += 1
                    m += 1
                # if greater than pivot, move nums[m] to the right side
                elif nums[m] > pivot:
                    nums[m], nums[r] = nums[r], nums[m]
                    r -= 1
                # if num[s] is a pivot value simply increment
                else:
                    m += 1

            # we found it...
            if l <= target_idx < m:
                # print(nums[p])
                return pivot
            # ...or it lies to the left of our pointer
            elif target_idx < l:
                return quickSelect(left, l - 1)
            # ...or to the right
            else:
                return quickSelect(m, right)

        # initial call, search whole nums list
        return quickSelect(left, right)

    # O(n) avg, O(n^2) worst but encounters runtime issues with some inputs
    # e.g. a significant number of repeated pivots
    def findKthLargestV1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        right = n - 1
        left = 0
        target_idx = n - k

        def quickSelect(left: int, right: int) -> int:
            p = left  # pointer
            pivot = random.randint(left, right)  # random pivot index

            # swap the random pivot number with the right
            nums[right], nums[pivot] = nums[pivot], nums[right]

            # iterate until we find a num that is greater than our pointer, then stop and swap
            for i in range(left, right):
                if nums[i] < nums[right]:  # remember right is now our pivot
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            # swap the pivot (in right) back to where it belongs
            nums[p], nums[right] = nums[right], nums[p]

            # we found it...
            if p == target_idx:
                # print(nums[p])
                return nums[p]

            # ...or it lies to the left of our pointer
            if p > target_idx:
                return quickSelect(left, p - 1)
            # ...or to the right
            else:
                return quickSelect(p + 1, right)

        # initial call, search whole nums list
        return quickSelect(left, right)


def test():
    solver = Solution()
    assert solver.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert solver.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert solver.findKthLargest([5, 2, 4, 1, 3, 6, 0], 4) == 3

    print("All tests passed!")


def testV1():
    solver = Solution()
    assert solver.findKthLargestV1([3, 2, 1, 5, 6, 4], 2) == 5
    assert solver.findKthLargestV1([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert solver.findKthLargestV1([5, 2, 4, 1, 3, 6, 0], 4) == 3

    print("All tests passed!")
