# 1047. Remove All Adjacent Duplicates In String


class Solution:
    def removeDuplicates(self, s: str) -> str:
        # stack of characters
        stack = []
        for letter in s:
            if stack and letter == stack[-1]:
                stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)


def test():
    solver = Solution()
    assert solver.removeDuplicates("abbaca") == "ca"
    assert solver.removeDuplicates("azxxzy") == "ay"
    print("All tests passed!")
