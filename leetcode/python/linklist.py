"""
Module for working with linked lists.
"""


class ListNode:
    """
    Definition for singly-linked list.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def init_looped_linked_list(values: list[int], pos: int = -1) -> ListNode:
    """
    Initialize a looped linked list based on the given values and position.

    :param values: List of values to form the linked list.
    :param pos: Position where tail of the list connects to create a loop.
                If pos is -1, then no cycle is formed.
    :return: The head of the newly formed linked list.
    """
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    loop = None

    i = 0
    for val in values[1:]:
        new_node = ListNode(val)
        current.next = new_node
        if i == pos:
            loop = current
        current = new_node
        i += 1
    if loop:
        current.next = loop

    return head


def values_from_linked_list(head: ListNode) -> list[int]:
    """
    Extract values from a linked list and return them in a list.

    :param head: The head node of the linked list.
    :return: List of values extracted from the linked list.
    """
    if not head:
        return []

    result = [head.val]
    while head.next:
        head = head.next
        result.append(head.val)
    return result
