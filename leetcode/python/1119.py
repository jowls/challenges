# 1119. Remove Vowels from a String
from typing import List


class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = set("aeiou")

        return "".join([letter for letter in s if letter not in vowels])


def test():
    solver = Solution()

    assert solver.removeVowels("leetcodeisacommunityforcoders") == "ltcdscmmntyfrcdrs"
    assert solver.removeVowels("aeiou") == ""

    print("All tests passed!")
