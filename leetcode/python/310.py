# 310. Minimum Height Trees

from collections import defaultdict
from math import inf
from typing import List


class Solution:
    # O(n)
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        edge_map = {i: [] for i in range(n)}

        for e in edges:
            edge_map[e[1]].append(e[0])
            edge_map[e[0]].append(e[1])

        print(edge_map)

        while len(edge_map) > 2:
            leaves = []

            for node in edge_map:
                if len(edge_map[node]) == 1:
                    leaves.append(node)

            for l in leaves:
                upstream_node = edge_map[l][0]
                edge_map[upstream_node].remove(l)
                del edge_map[l]

        return [e for e in edge_map]


def test():
    solver = Solution()

    assert solver.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]) == [1]
    assert solver.findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]) == [
        3,
        4,
    ]

    print("All tests passed!")
