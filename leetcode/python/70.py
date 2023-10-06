# 70. Climbing Stairs


class Solution:
    # O(n) bottom-up
    def climbStairs(self, n: int) -> int:
        first, second = 1, 1

        for i in range(n - 1):
            first, second = first + second, first

        return first

    # O(n) top-down
    def climbStairsV1(self, n: int) -> int:
        memo = [0] * (n + 1)

        def dfs(n, memo):
            if n == 0:
                return 1
            elif n < 0:
                return 0
            elif memo[n]:
                return memo[n]

            memo[n] = dfs(n - 1, memo) + dfs(n - 2, memo)

            return memo[n]

        return dfs(n, memo)


def test():
    solver = Solution()

    assert solver.climbStairs(2) == 2
    assert solver.climbStairs(3) == 3

    print("All tests passed!")
