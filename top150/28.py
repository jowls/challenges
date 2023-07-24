# 28. Find the Index of the First Occurrence in a String

# Given two strings needle and haystack, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.

import re

example1_arg1 = "sadbutsad"
example1_arg2 = "sad"
example1_out = 0

example2_arg1 = "leetcode"
example2_arg2 = "leeto"
example2_out = -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        match = re.search(needle, haystack)
        if match:
            return match.start()
        return -1


print(Solution().strStr(example1_arg1, example1_arg2) == example1_out)
print(Solution().strStr(example2_arg1, example2_arg2) == example2_out)
