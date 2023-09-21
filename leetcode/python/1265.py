# 1265. Print Immutable Linked List in Reverse

from typing import List


class ImmutableListNode:
    def __init__(self, val: int, next: "ImmutableListNode" = None):
        self._value = val
        self._next = next

    def printValue(self) -> None:
        print(self._value)

    def getNext(self) -> "ImmutableListNode":
        return self._next


class Solution:
    # O(n)
    def printLinkedListInReverse(self, head: "ImmutableListNode") -> None:
        def printAllNodes(node):
            if node is None:
                return
            printAllNodes(node.getNext())
            node.printValue()

        printAllNodes(head)


def construct_linked_list(values: List[int]) -> ImmutableListNode:
    if not values:
        return None
    head = current = ImmutableListNode(values[0])
    for value in values[1:]:
        current._next = ImmutableListNode(value)
        current = current._next
    return head


def test_example_1(capsys):
    head = construct_linked_list([1, 2, 3, 4])

    solver = Solution()
    solver.printLinkedListInReverse(head)

    captured = capsys.readouterr()
    assert captured.out == "4\n3\n2\n1\n"


def test_example_2(capsys):
    head = construct_linked_list([0, -4, -1, 3, -5])

    solver = Solution()
    solver.printLinkedListInReverse(head)

    captured = capsys.readouterr()
    assert captured.out == "-5\n3\n-1\n-4\n0\n"


def test_example_3(capsys):
    head = construct_linked_list([-2, 0, 6, 4, 4, -6])

    solver = Solution()
    solver.printLinkedListInReverse(head)

    captured = capsys.readouterr()
    assert captured.out == "-6\n4\n4\n6\n0\n-2\n"
