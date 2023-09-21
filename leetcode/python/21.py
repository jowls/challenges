# 21. Merge Two Sorted Listsclass Solution:

from typing import Optional
from linklist import ListNode, init_looped_linked_list, values_from_linked_list


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2
        # print(values_from_linked_list(dummy.next))
        return dummy.next


def test():
    solver = Solution()

    # example 1
    list1 = init_looped_linked_list([1, 2, 4])
    list2 = init_looped_linked_list([1, 3, 4])
    merged_list = solver.mergeTwoLists(list1, list2)
    assert values_from_linked_list(merged_list) == [1, 1, 2, 3, 4, 4]

    # example 2
    list1 = init_looped_linked_list([])
    list2 = init_looped_linked_list([])
    merged_list = solver.mergeTwoLists(list1, list2)
    assert values_from_linked_list(merged_list) == []

    # example 3
    list1 = init_looped_linked_list([])
    list2 = init_looped_linked_list([0])
    merged_list = solver.mergeTwoLists(list1, list2)
    assert values_from_linked_list(merged_list) == [0]

    print("All tests passed!")
