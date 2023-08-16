# 58. Length of Last Word
#
# Given a string s consisting of words and spaces, return the length of the
# last word in the string. A word is a maximal substring consisting of
# non-space characters only.

example1_arg1 = "Hello World"
example1_out = 5

example2_arg1 = "   fly me   to   the moon  "
example2_out = 4

example3_arg1 = "luffy is still joyboy"
example3_out = 6


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split()
        return len(word_list[-1])


print(Solution().lengthOfLastWord(example1_arg1) == example1_out)
print(Solution().lengthOfLastWord(example2_arg1) == example2_out)
print(Solution().lengthOfLastWord(example3_arg1) == example3_out)
