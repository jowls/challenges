# 39. Combination Sum

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(target, path, start):
            if target == 0:
                results.append(path[:])
                return
            elif target < 0:
                return

            # give i a chance to repeat
            for i in range(start, len(candidates)):
                dfs(target - candidates[i], path + [candidates[i]], i)

        dfs(target, [], 0)

        # print(results)
        return results


def test():
    solver = Solution()

    assert sorted(solver.combinationSum([2, 3, 6, 7], 7)) == sorted([[7], [2, 2, 3]])
    assert sorted(solver.combinationSum([2, 3, 5], 8)) == sorted(
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    )
    assert sorted(solver.combinationSum([2], 1)) == sorted([])

    print("All tests passed!")
