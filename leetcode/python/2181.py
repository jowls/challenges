# 2181. Merge Nodes in Between Zeros

from typing import Optional
from linklist import ListNode, init_looped_linked_list, values_from_linked_list


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = head.next
        running_total = 0
        while cur.next:
            running_total += cur.val
            if cur.next.val == 0:
                cur.val = running_total
                prev.next = cur
                prev = cur
                running_total = 0
            cur = cur.next

        prev.next = None
        return head.next


def test():
    solver = Solution()

    head = init_looped_linked_list([0, 3, 1, 0, 4, 5, 2, 0])
    expected_output = [4, 11]
    assert values_from_linked_list(solver.mergeNodes(head)) == expected_output

    head = init_looped_linked_list([0, 1, 0, 3, 0, 2, 2, 0])
    expected_output = [1, 3, 4]
    assert values_from_linked_list(solver.mergeNodes(head)) == expected_output

    print("All tests passed!")
