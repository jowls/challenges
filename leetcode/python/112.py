# 112. Path Sum

from bintree import TreeNode, init_binary_tree
from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        # tree depth-first search O(n)
        if root.left is None and root.right is None:
            if root.val == targetSum:
                return True
        if root.left:
            if self.hasPathSum(root.left, targetSum - root.val):
                return True
        if root.right:
            if self.hasPathSum(root.right, targetSum - root.val):
                return True

        return False


def test():
    solver = Solution()

    root = init_binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    assert solver.hasPathSum(root, 22) == True

    root = init_binary_tree([1, 2, 3])
    assert solver.hasPathSum(root, 5) == False

    root = init_binary_tree([])
    assert solver.hasPathSum(root, 0) == False

    # Add more tests if needed
    print("All tests passed!")
