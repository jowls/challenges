# 23. Merge k Sorted Lists

from typing import List, Optional
from linklist import ListNode, init_looped_linked_list, values_from_linked_list


class Solution:
    # O(n logk)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return []

        # loop until we've merged all lists into one
        while len(lists) > 1:
            temp = []

            # two list at a time
            for i in range(0, len(lists), 2):
                l1 = lists[i]

                # l2 might be null if we have an odd number of lists
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                temp.append(self.mergeTwoLists(l1, l2))

            # update lists to contain our merged lists
            lists = temp

        return lists[0]

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

        return dummy.next

    # O(nk)
    def mergeKListsV1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy

        # filter out empty lists
        lists = [l for l in lists if l]

        while lists:
            # find list with smallest head value and update pointers
            i, cur = min(enumerate(lists), key=lambda x: x[1].val)
            prev.next = cur
            prev = cur
            lists[i] = lists[i].next

            # if list is exhauseted, remove it
            if not lists[i]:
                lists.pop(i)

        return dummy.next


def test():
    solver = Solution()

    # example 1
    list1 = init_looped_linked_list([1, 4, 5])
    list2 = init_looped_linked_list([1, 3, 4])
    list3 = init_looped_linked_list([2, 6])
    merged_list = solver.mergeKLists([list1, list2, list3])
    assert values_from_linked_list(merged_list) == [1, 1, 2, 3, 4, 4, 5, 6]

    # example 2
    assert not solver.mergeKLists([])

    # example 3
    empty_list = init_looped_linked_list([])
    assert not solver.mergeKLists([empty_list])

    print("All tests passed!")


def testV1():
    solver = Solution()

    # example 1
    list1 = init_looped_linked_list([1, 4, 5])
    list2 = init_looped_linked_list([1, 3, 4])
    list3 = init_looped_linked_list([2, 6])
    merged_list = solver.mergeKListsV1([list1, list2, list3])
    assert values_from_linked_list(merged_list) == [1, 1, 2, 3, 4, 4, 5, 6]

    # example 2
    assert not solver.mergeKListsV1([])

    # example 3
    empty_list = init_looped_linked_list([])
    assert not solver.mergeKListsV1([empty_list])

    print("All tests passed!")
