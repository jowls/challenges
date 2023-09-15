# 113. Path Sum II

from bintree import TreeNode, init_binary_tree
from typing import List, Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node: Optional[TreeNode], path: List[int], remaining_sum: int):
            if not node:
                return

            # keep track of where we are in the path
            path.append(node.val)
            # and the remaining sum
            remaining_sum -= node.val

            if not node.left and not node.right:
                if remaining_sum == 0:
                    # append COPY of list to results
                    result.append(path[:])

            # continue the search down both branches
            dfs(node.left, path, remaining_sum)
            dfs(node.right, path, remaining_sum)

            # backtrack
            path.pop()

        dfs(root, [], targetSum)

        return result


def test():
    solver = Solution()

    root = init_binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    assert solver.pathSum(root, 22) == [[5, 4, 11, 2], [5, 8, 4, 5]]

    root = init_binary_tree([1, 2, 3])
    assert solver.pathSum(root, 5) == []

    root = init_binary_tree([1, 2])
    assert solver.pathSum(root, 0) == []

    print("All tests passed!")
