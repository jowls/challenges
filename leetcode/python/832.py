# 832. Flipping an Image

from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        def reverseAndInvertRow(row: List[int]) -> List[int]:
            n = len(row)

            # handle the centre element if odd
            if n % 2 != 0:
                row[n // 2] = 0 if row[n // 2] else 1

            # flip the rest using two pointers
            for i in range(n // 2):
                j = n - i - 1
                l = 0 if row[i] else 1
                r = 0 if row[j] else 1
                row[i], row[j] = r, l

            return row

        result = []
        for row in image:
            result.append(reverseAndInvertRow(row))
        return result


def test():
    solver = Solution()
    assert solver.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]) == [
        [1, 0, 0],
        [0, 1, 0],
        [1, 1, 1],
    ]
    assert solver.flipAndInvertImage(
        [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    ) == [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
    print("All tests passed!")
