# 2469. Convert the Temperature

from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32]


def test():
    solver = Solution()

    assert abs(solver.convertTemperature(36.50)[0] - 309.65000) < 1e-5
    assert abs(solver.convertTemperature(36.50)[1] - 97.70000) < 1e-5

    assert abs(solver.convertTemperature(122.11)[0] - 395.26000) < 1e-5
    assert abs(solver.convertTemperature(122.11)[1] - 251.79800) < 1e-5

    print("All tests passed!")
