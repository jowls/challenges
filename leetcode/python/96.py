# 96. Reverse Linked List II

from typing import List, Optional

example1_arg1 = [1, 2, 3, 4, 5]
example1_arg2 = -1
example1_arg3 = 2
example1_arg4 = 4
example1_out = [1, 4, 3, 2, 5]

example2_arg1 = [5]
example2_arg2 = -1
example2_arg3 = 1
example2_arg4 = 1
example2_out = [5]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if head.next == None:
            # swap return comment for submission after local testing
            return values_from_linked_list(head)
            # return head

        l = left - 1  # zero-indexed left
        r = right - 1  # zero-indexed right
        fake_head = ListNode(0)
        fake_head.next = head
        prev = fake_head
        cur = head

        # advance current to where the reversal will begin
        for _ in range(0, l):
            cur = cur.next
            prev = prev.next

        tail_of_front = prev

        # reverse desired portion
        prev = None
        for _ in range(right - left + 1):
            temp_next = cur.next
            cur.next = prev
            prev = cur
            cur = temp_next

        # set the new tail of the reversed list to the head of the back-end unmodified remainder
        tail_of_front.next.next = cur
        # then point the tail of the front unmodified list to the new head of the reversed list
        tail_of_front.next = prev

        # swap return comment for submission after local testing
        return values_from_linked_list(fake_head.next)
        # return fake_head.next

    def reverseBetweenV1(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        values = []
        idx = 0
        l = left - 1  # zero-indexed left
        r = right - 1  # zero-indexed right
        start_reverse_node = None
        cur = head
        while idx <= r:
            if idx == l:
                start_reverse_node = cur
            if idx >= l:
                values.append(cur.val)
            cur = cur.next
            idx += 1
        print(values)
        cur = start_reverse_node
        for v in reversed(values):
            cur.val = v
            cur = cur.next

        # swap return comment for submission after local testing
        # return head
        print(values_from_linked_list(head))
        return values_from_linked_list(head)


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


def values_from_linked_list(head):
    result = [head.val]
    while head.next:
        head = head.next
        result.append(head.val)
    return result


print(
    Solution().reverseBetween(
        init_looped_linked_list(example1_arg1, example1_arg2),
        example1_arg3,
        example1_arg4,
    )
    == example1_out
)
print(
    Solution().reverseBetween(
        init_looped_linked_list(example2_arg1, example2_arg2),
        example2_arg3,
        example2_arg4,
    )
    == example2_out
)
