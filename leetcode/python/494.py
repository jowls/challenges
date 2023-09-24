from typing import List


# 494. Target Sum
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # init cache for optimization
        memo = {}

        # recursively count the number of ways we can achieve the target
        def dfs(total: int, depth: int):
            if (total, depth) in memo:
                return memo[(total, depth)]
            if depth == len(nums):
                return 1 if total == target else 0

            pos_total = total + nums[depth]
            neg_total = total - nums[depth]
            count = dfs(pos_total, depth + 1) + dfs(neg_total, depth + 1)

            return count

        count = dfs(0, 0)
        # print(count)
        return count


def test():
    solver = Solution()

    assert solver.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
    assert solver.findTargetSumWays([1], 1) == 1

    print("All tests passed!")
