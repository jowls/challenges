# 2487. Remove Nodes From Linked List

from typing import List, Optional
from math import inf
from linklist import ListNode, init_looped_linked_list, values_from_linked_list


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy first node to prepend with val of positive infinity
        dummy = ListNode(float(inf), head)
        cur = head
        # monotonically decreasing (by node.val)
        stack = [dummy]

        while cur:
            while stack and cur.val > stack[-1].val:
                stack.pop()
                stack[-1].next = cur
            stack.append(cur)
            cur = cur.next

        # uncomment the line below during submission
        # return dummy.next

        # comment or remove this before submission
        return values_from_linked_list(dummy.next)


def test():
    solver = Solution()
    assert solver.removeNodes(init_looped_linked_list([5, 2, 13, 3, 8])) == [13, 8]
    assert solver.removeNodes(init_looped_linked_list([1, 1, 1, 1])) == [1, 1, 1, 1]
    print("All tests passed!")


test()
