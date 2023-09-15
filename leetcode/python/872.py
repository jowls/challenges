# 872. Leaf-Similar Trees

from bintree import TreeNode, init_binary_tree
from typing import Optional


class Solution:
    # O(n)
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq = []

        def dfs(root: Optional[TreeNode]):
            if not root.left and not root.right:
                seq.append(root.val)
                return
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

        dfs(root1)
        root1_seq = seq[:]
        seq.clear()
        dfs(root2)
        root2_seq = seq[:]

        return root1_seq == root2_seq


def test():
    solver = Solution()
    assert (
        solver.leafSimilar(
            init_binary_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]),
            init_binary_tree(
                [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
            ),
        )
        == True
    )
    assert (
        solver.leafSimilar(init_binary_tree([1, 2, 3]), init_binary_tree([1, 3, 2]))
        == False
    )
    print("All tests passed!")
