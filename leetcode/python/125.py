# 125. Valid Palindrome
#
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. Alphanumeric characters include letters and
# numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

import re

example1_arg1 = "A man, a plan, a canal: Panama"
example1_out = True

example2_arg1 = "race a car"
example2_out = False

example3_arg1 = " "
example3_out = True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        # print(lower)
        pattern = re.compile('[^a-zA-Z0-9]')
        alphanum_lower = re.sub(pattern, '', lower)
        # print(alphanum_lower)
        if alphanum_lower == alphanum_lower[::-1]:
            return True
        else:
            return False


print(Solution().isPalindrome(example1_arg1) == example1_out)
print(Solution().isPalindrome(example2_arg1) == example2_out)
print(Solution().isPalindrome(example3_arg1) == example3_out)
