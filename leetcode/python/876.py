# 876. Middle of the Linked List

from typing import List, Optional

example1_arg1 = [1, 2, 3, 4, 5]
example1_arg2 = -1
example1_out = 3


example2_arg1 = [1, 2, 3, 4, 5, 6]
example2_arg2 = -1
example2_out = 4


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = head
        f = head

        while f and f.next:
            s = s.next
            f = f.next.next
        return s.val


def init_looped_linked_list(values, pos):
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


print(
    Solution().middleNode(init_looped_linked_list(example1_arg1, example1_arg2))
    == example1_out
)
print(
    Solution().middleNode(init_looped_linked_list(example2_arg1, example2_arg2))
    == example2_out
)
