# 111. Minimum Depth of Binary Tree

from bintree import TreeNode, init_binary_tree
from typing import Optional
from collections import deque


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        depth = 0
        q.append(root)

        # tree breadth first search O(n)
        while q:
            depth += 1
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()
                if node:
                    if not node.left and not node.right:
                        return depth
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)


def test():
    solver = Solution()

    root = init_binary_tree([3, 9, 20, None, None, 15, 7])
    assert solver.minDepth(root) == 2

    root = init_binary_tree([2, None, 3, None, 4, None, 5, None, 6])
    assert solver.minDepth(root) == 5

    print("All tests passed!")
