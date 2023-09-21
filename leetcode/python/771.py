# 771. Jewels and Stones


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x = 0
        for s in stones:
            if s in jewels:
                x += 1
        return x


def test():
    solver = Solution()

    assert solver.numJewelsInStones("aA", "aAAbbbb") == 3
    assert solver.numJewelsInStones("z", "ZZ") == 0

    print("All tests passed!")
