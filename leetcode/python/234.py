# 234. Palindrome Linked List

from typing import List, Optional

example1_arg1 = [1, 2, 2, 1]
example1_arg2 = -1
example1_out = True

example2_arg1 = [1, 2]
example2_arg2 = -1
example2_out = False


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        start = []
        s = f = head
        while f and f.next:
            start.append(s.val)
            s = s.next
            f = f.next.next
        if f == None:
            for i in reversed(start):
                if s.val != i:
                    return False
                s = s.next
        else:
            start.append(s.val)
            print(start)
            for i in reversed(start):
                if s.val != i:
                    return False
                s = s.next
        return True


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
    Solution().isPalindrome(init_looped_linked_list(example1_arg1, example1_arg2))
    == example1_out
)
print(
    Solution().isPalindrome(init_looped_linked_list(example2_arg1, example2_arg2))
    == example2_out
)
