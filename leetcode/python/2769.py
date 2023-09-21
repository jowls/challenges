# 2769. Find the Maximum Achievable Number


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t * 2


def test():
    solver = Solution()

    assert solver.theMaximumAchievableX(4, 1) == 6
    assert solver.theMaximumAchievableX(3, 2) == 7

    print("All tests passed!")
