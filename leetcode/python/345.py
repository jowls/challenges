# 345. Reverse Vowels of a String

from typing import List

example1_arg1 = "hello"
example1_out = "holle"

example2_arg1 = "leetcode"
example2_out = "leotcede"

example3_arg1 = "race car"
example3_out = "race car"


class Solution:
    def reverseVowelsV1(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        idxs = []
        for idx, letter in enumerate(s):
            if letter.lower() in vowels:
                idxs.append(idx)
        i = 0
        j = len(idxs) - 1
        temp_s = s
        if len(idxs) > 1:
            l = idxs[i]
            r = idxs[j]
            while l < r:
                temp_s = temp_s[:l] + s[r] + temp_s[l + 1 : r] + s[l] + temp_s[r + 1 :]
                i += 1
                j -= 1
                l = idxs[i]
                r = idxs[j]
        return temp_s

    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        i = 0
        j = len(s) - 1
        list_s = list(s)
        while i < j:
            while i < j and vowels.find(list_s[i]) == -1:
                i += 1
            while i < j and vowels.find(list_s[j]) == -1:
                j -= 1
            list_s[i], list_s[j] = list_s[j], list_s[i]
            i += 1
            j -= 1
        return "".join(list_s)


print(Solution().reverseVowels(example1_arg1) == example1_out)
print(Solution().reverseVowels(example2_arg1) == example2_out)
print(Solution().reverseVowels(example3_arg1) == example3_out)
