# 1079. Letter Tile Possibilities


class Solution:
    # O(n!)
    def numTilePossibilities(self, tiles: str) -> int:
        results = set()

        def backtrack(tiles: str, combo: str):
            if len(combo):
                results.add(combo)

            for i in range(len(tiles)):
                # "use" tiles[i]
                backtrack(tiles[:i] + tiles[i + 1 :], combo + tiles[i])

        backtrack(tiles, "")

        return len(results)


def test():
    solver = Solution()

    assert solver.numTilePossibilities("AAB") == 8
    assert solver.numTilePossibilities("AAABBC") == 188
    assert solver.numTilePossibilities("V") == 1

    print("All tests passed!")
