# 206. Reverse Linked List

from typing import List, Optional
from linklist import ListNode, init_looped_linked_list, values_from_linked_list

example1_arg1 = [1, 2, 3, 4, 5]
example1_out = [5, 4, 3, 2, 1]

example2_arg1 = [1, 2]
example2_out = [2, 1]


class Solution:
    def reverseListIterative(self, head: Optional[ListNode]) -> ListNode:
        if not head:
            return None

        cur = head
        prev = None

        while cur:
            # save the next node into temp before reversing the current
            temp = cur.next
            # reverse current
            cur.next = prev
            # advance pointers along the list
            prev = cur
            cur = temp

        # swap return comment for submission after local testing
        # return prev
        return values_from_linked_list(prev)

    def reverseListRecursive(self, head: Optional[ListNode]) -> ListNode:
        if not head:
            return None

        reversed_head = None

        def reverse_nodes(node, prev):
            # if last node of list
            if not node.next:
                nonlocal reversed_head
                node.next = prev
                # tail of original list becomes head of reversed list
                reversed_head = node
            # else recurse to the next node
            else:
                reverse_nodes(node.next, node)
                # once recursive call completes, update current node.next to prev
                node.next = prev

        reverse_nodes(head, None)

        # swap return comment for submission after local testing
        # return reversed_head
        return values_from_linked_list(reversed_head)


print(
    Solution().reverseListIterative(init_looped_linked_list(example1_arg1))
    == example1_out
)
print(
    Solution().reverseListIterative(init_looped_linked_list(example2_arg1))
    == example2_out
)

print(
    Solution().reverseListRecursive(init_looped_linked_list(example1_arg1))
    == example1_out
)
print(
    Solution().reverseListRecursive(init_looped_linked_list(example2_arg1))
    == example2_out
)
