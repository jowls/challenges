# 496. Next Greater Element I

from typing import List


class Solution:
    # O(n + m) one-pass solution
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # where to store each result in the result array
        result_pos = {a: i for i, a in enumerate(nums1)}
        # init empty result array
        result = [-1] * len(nums1)
        # stack will be monotonic decreasing
        stack = []

        for i, a in enumerate(nums2):
            while stack and a > stack[-1]:
                val = stack.pop()
                result[result_pos[val]] = a
            if a in result_pos:
                stack.append(a)

        return result

    # O(n * m) nested solution
    def nextGreaterElementV1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # where to store each result in the result array
        result_pos = {a: i for i, a in enumerate(nums1)}
        # init empty result array
        result = [-1] * len(nums1)

        for i, a in enumerate(nums2):
            # if this a number we have to report on, search the rest of the array
            if a in result_pos:
                for b in nums2[i + 1 :]:
                    if b > a:
                        result[result_pos[a]] = b
                        break

        return result


def test():
    solver = Solution()

    assert solver.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert solver.nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]

    assert solver.nextGreaterElementV1([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert solver.nextGreaterElementV1([2, 4], [1, 2, 3, 4]) == [3, -1]

    print("All tests passed!")
