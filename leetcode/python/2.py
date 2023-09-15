# 2. Add Two Numbers
from typing import Optional
from linklist import ListNode, init_looped_linked_list, values_from_linked_list


class Solution:
    # O(max(m,n))
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        dummy = ListNode()
        cur = dummy
        carry = 0

        while node1 or node2 or carry:
            one = node1.val if node1 else 0
            two = node2.val if node2 else 0

            out = one + two + carry
            carry = out // 10
            out = out % 10

            cur.next = ListNode(out)
            cur = cur.next

            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None

        # uncomment line below for submission
        # return dummy.next

        # comment or remove below before submission
        return values_from_linked_list(dummy.next)


def test():
    solver = Solution()
    assert solver.addTwoNumbers(
        init_looped_linked_list([2, 4, 3]), init_looped_linked_list([5, 6, 4])
    ) == [7, 0, 8]
    assert solver.addTwoNumbers(
        init_looped_linked_list([0]), init_looped_linked_list([0])
    ) == [0]
    assert solver.addTwoNumbers(
        init_looped_linked_list([9, 9, 9, 9, 9, 9, 9]),
        init_looped_linked_list([9, 9, 9, 9]),
    ) == [8, 9, 9, 9, 0, 0, 0, 1]
    print("All tests passed!")
