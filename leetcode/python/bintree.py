"""
Module for working with binary trees.
"""


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def init_binary_tree(values: list[int]) -> TreeNode:
    """
    Initialize a binary tree based on the given values using level order traversal.

    :param values: List of values to form the binary tree. Use 'None' for missing nodes.
    """
    if not values:
        return None

    # Create a queue to hold nodes to be processed.
    queue = []

    # Start with the root node.
    root = TreeNode(values[0])
    queue.append(root)

    # Track the position in the values list.
    i = 1

    # While there are nodes left to process:
    while queue and i < len(values):
        current_node = queue.pop(0)

        # Process the left child.
        if i < len(values) and values[i] is not None:
            left_node = TreeNode(values[i])
            current_node.left = left_node
            queue.append(left_node)
        i += 1

        # Process the right child.
        if i < len(values) and values[i] is not None:
            right_node = TreeNode(values[i])
            current_node.right = right_node
            queue.append(right_node)
        i += 1

    return root
