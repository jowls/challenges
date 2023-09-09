# 876. Middle of the Linked List

from typing import List, Optional
from linklist import ListNode, init_looped_linked_list

example1_arg1 = [1, 2, 3, 4, 5]
example1_arg2 = -1
example1_out = 3


example2_arg1 = [1, 2, 3, 4, 5, 6]
example2_arg2 = -1
example2_out = 4


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = head
        f = head

        while f and f.next:
            s = s.next
            f = f.next.next
        return s.val


print(
    Solution().middleNode(init_looped_linked_list(example1_arg1, example1_arg2))
    == example1_out
)
print(
    Solution().middleNode(init_looped_linked_list(example2_arg1, example2_arg2))
    == example2_out
)
