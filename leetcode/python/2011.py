# 2011. Final Value of Variable After Performing Operations

from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for o in operations:
            if "--" in o:
                result -= 1
            elif "++" in o:
                result += 1
        return result


def test():
    solver = Solution()

    assert solver.finalValueAfterOperations(["--X", "X++", "X++"]) == 1
    assert solver.finalValueAfterOperations(["++X", "++X", "X++"]) == 3
    assert solver.finalValueAfterOperations(["X++", "++X", "--X", "X--"]) == 0

    print("All tests passed!")
