# 1302. Deepest Leaves Sum

from typing import Optional
from bintree import TreeNode, init_binary_tree


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_depth_seen = 0

        def dfs(node, depth):
            nonlocal max_depth_seen

            # base case
            if not node:
                return
            # keep track globally of how deep we've seen
            current_depth = depth + 1
            if current_depth > max_depth_seen:
                max_depth_seen = current_depth

            # if we're at a leaf node, return a tuple of val, depth for later evaluation
            if not node.left and not node.right:
                yield (node.val, current_depth)

            # continue the search down both branches
            if node.left:
                yield from dfs(node.left, current_depth)
            if node.right:
                yield from dfs(node.right, current_depth)

        # exhaust the generator to a list so it can be used in the list comprehension below
        results = list(dfs(root, 0))

        deepest_vals = [x[0] for x in results if x[1] == max_depth_seen]

        return sum(deepest_vals)


def test():
    solver = Solution()

    tree = init_binary_tree([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])
    assert solver.deepestLeavesSum(tree) == 15

    tree = init_binary_tree([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])
    assert solver.deepestLeavesSum(tree) == 19

    print("All tests passed!")
