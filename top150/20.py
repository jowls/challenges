# 20. Valid Parentheses
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid. An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

example1_arg1 = "()"
example1_out = True

example2_arg1 = "()[]{}"
example2_out = True

example3_arg1 = "(]"
example3_out = False


class Solution:
    def isValid(self, s: str) -> bool:
        expected_close = []
        for letter in s:
            if letter == '(':
                expected_close.append(')')
            elif letter == '{':
                expected_close.append('}')
            elif letter == '[':
                expected_close.append(']')

            if len(expected_close) < 1:
                return False

            if letter == ')':
                if not expected_close.pop() == ')':
                    return False
            elif letter == '}':
                if not expected_close.pop() == '}':
                    return False
            elif letter == ']':
                if not expected_close.pop() == ']':
                    return False
        if len(expected_close) == 0:
            return True
        else:
            return False


print(Solution().isValid(example1_arg1) == example1_out)
print(Solution().isValid(example2_arg1) == example2_out)
print(Solution().isValid(example3_arg1) == example3_out)
