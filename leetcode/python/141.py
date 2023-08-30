# 141. Linked List Cycle

from typing import List, Optional

example1_arg1 = [3, 2, 0, -4]
example1_arg2 = 1
example1_out = True

example2_arg1 = [1, 2]
example2_arg2 = 0
example2_out = True

example3_arg1 = [1]
example3_arg2 = -1
example3_out = False

example4_arg1 = []
example4_arg2 = -1
example4_out = False

example5_arg1 = [
    -21,
    10,
    17,
    8,
    4,
    26,
    5,
    35,
    33,
    -7,
    -16,
    27,
    -12,
    6,
    29,
    -12,
    5,
    9,
    20,
    14,
    14,
    2,
    13,
    -24,
    21,
    23,
    -21,
    5,
]
example5_arg2 = -1
example5_out = False


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        s = head
        f = head

        while f and f.next:
            s = s.next
            f = f.next.next
            if f == s:
                return True
        return False


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
    Solution().hasCycle(init_looped_linked_list(example1_arg1, example1_arg2))
    == example1_out
)
print(
    Solution().hasCycle(init_looped_linked_list(example2_arg1, example2_arg2))
    == example2_out
)
print(
    Solution().hasCycle(init_looped_linked_list(example3_arg1, example3_arg2))
    == example3_out
)
print(
    Solution().hasCycle(init_looped_linked_list(example4_arg1, example4_arg2))
    == example4_out
)
print(
    Solution().hasCycle(init_looped_linked_list(example5_arg1, example5_arg2))
    == example5_out
)
