# 142. Linked List Cycle II

from typing import List, Optional
from linklist import ListNode, init_looped_linked_list

example1_arg1 = [3, 2, 0, -4]
example1_arg2 = 1
example1_out = 1

example2_arg1 = [1, 2]
example2_arg2 = 0
example2_out = 0

example3_arg1 = [1]
example3_arg2 = -1
example3_out = None

example4_arg1 = []
example4_arg2 = -1
example4_out = None

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
example5_out = None


class Solution:
    def detectCycleV1(self, head: Optional[ListNode]) -> bool:
        if not head:
            return None
        nodes = {}
        s = head
        nodes[s] = 0
        i = 0
        while s.next:
            s = s.next
            i += 1
            if s in nodes:
                return nodes[s]
            else:
                nodes[s] = i
        return None

    def checkIntersect(self, head: Optional[ListNode]) -> ListNode:
        if head == None or head.next == None:
            return None
        f = s = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return s
        return None

    # O(1) space complexity
    def detectCycle(self, head: Optional[ListNode]) -> bool:
        intersect = self.checkIntersect(head)
        if not intersect:
            return None
        start = head
        i = 0
        while start != intersect:
            start = start.next
            intersect = intersect.next
            i += 1
        # return intersect
        print(i)
        return i


print(
    Solution().detectCycle(init_looped_linked_list(example1_arg1, example1_arg2))
    == example1_out
)
print(
    Solution().detectCycle(init_looped_linked_list(example2_arg1, example2_arg2))
    == example2_out
)
print(
    Solution().detectCycle(init_looped_linked_list(example3_arg1, example3_arg2))
    == example3_out
)
print(
    Solution().detectCycle(init_looped_linked_list(example4_arg1, example4_arg2))
    == example4_out
)
print(
    Solution().detectCycle(init_looped_linked_list(example5_arg1, example5_arg2))
    == example5_out
)
