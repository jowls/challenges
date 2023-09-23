# 416. Partition Equal Subset Sum

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # init the set, plus we can always create 0 no matter what's in nums
        sums = set()
        sums.add(0)

        # if the array has an odd sum it's impossible
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2

        # track possible sums
        for n in nums:
            temp_sums = sums.copy()
            for s in sums:
                temp_sums.add(s + n)
            sums = temp_sums

        # print(sums)
        return True if target in sums else False


def test():
    solver = Solution()

    assert solver.canPartition([1, 5, 11, 5]) == True
    assert solver.canPartition([1, 2, 3, 5]) == False

    print("All tests passed!")
