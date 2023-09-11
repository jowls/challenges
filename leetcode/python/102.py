# 102. Binary Tree Level Order Traversal

from bintree import TreeNode, init_binary_tree
from typing import List, Optional
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = deque()
        q.append(root)

        # tree breadth first search O(n)
        while q:
            level = []
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if level:
                result.append(level)
        print(result)
        return result


def test():
    solver = Solution()

    root = init_binary_tree([3, 9, 20, None, None, 15, 7])
    assert solver.levelOrder(root) == [[3], [9, 20], [15, 7]]

    root = init_binary_tree([1])
    assert solver.levelOrder(root) == [[1]]

    root = init_binary_tree([])
    assert solver.levelOrder(root) == []

    root = init_binary_tree([2, None, 3, None, 4, None, 5, None, 6])
    assert solver.levelOrder(root) == [[2], [3], [4], [5], [6]]

    print("All tests passed!")
