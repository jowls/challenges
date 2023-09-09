# 25. Reverse Nodes in k-Group

from typing import List, Optional
from linklist import ListNode, init_looped_linked_list, values_from_linked_list

example1_arg1 = [1, 2, 3, 4, 5]
example1_arg2 = 2
example1_out = [2, 1, 4, 3, 5]

example2_arg1 = [1, 2, 3, 4, 5]
example2_arg2 = 3
example2_out = [3, 2, 1, 4, 5]


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head.next == None:
            return head

        # calculate the number of k reversal loops required
        count = 1
        cur = head
        while cur.next:
            cur = cur.next
            count += 1
        required_loops = count // k

        # dummy setup
        fake_head = ListNode(0, next=head)

        # initialize two working pointers
        prev, cur = None, head

        # this will be updated to represent the node immediately prior to the section of list currently being reversed
        tail_of_front = fake_head

        # loop the calculated number of times to reverse all k-groups
        for i in range(required_loops):
            # save the old tail before modifying, it will eventually be the new head of the k-group when reversed
            old_tail_of_front = tail_of_front

            # the current node before any operations will eventually be the new tail of the k-group when reversed
            tail_of_front = cur

            # reverse the current k-group
            for j in range(k):
                temp_next = cur.next
                cur.next = prev
                prev = cur
                cur = temp_next
            # handle the edge integration of the reversed k-group
            old_tail_of_front.next = prev
            prev = tail_of_front
        # append the rest of the list to the end
        tail_of_front.next = cur

        # swap return comment for submission after local testing
        # print(values_from_linked_list(fake_head.next))
        return values_from_linked_list(fake_head.next)
        # return fake_head.next


print(
    Solution().reverseKGroup(init_looped_linked_list(example1_arg1), example1_arg2)
    == example1_out
)
print(
    Solution().reverseKGroup(init_looped_linked_list(example2_arg1), example2_arg2)
    == example2_out
)
