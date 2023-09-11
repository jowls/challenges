# 107. Binary Tree Level Order Traversal II

from bintree import TreeNode, init_binary_tree
from typing import List, Optional
from collections import deque


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        result.reverse()
        return result


def test():
    solver = Solution()

    root = init_binary_tree([3, 9, 20, None, None, 15, 7])
    assert solver.levelOrderBottom(root) == [[15, 7], [9, 20], [3]]

    root = init_binary_tree([1])
    assert solver.levelOrderBottom(root) == [[1]]

    root = init_binary_tree([])
    assert solver.levelOrderBottom(root) == []

    print("All tests passed!")
