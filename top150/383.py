# 383. Ransom Note
#
# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed by using the letters from magazine and false otherwise. Each
# letter in magazine can only be used once in ransomNote.

example1_arg1 = "a"
example1_arg2 = "b"
example1_out = False

example2_arg1 = "aa"
example2_arg2 = "ab"
example2_out = False

example3_arg1 = "aa"
example3_arg2 = "aab"
example3_out = True


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = {}
        ran_dict = {}
        for letter in magazine:
            if letter in mag_dict:
                mag_dict[letter] += 1
            else:
                mag_dict[letter] = 1
        for letter in ransomNote:
            if letter in ran_dict:
                ran_dict[letter] += 1
            else:
                ran_dict[letter] = 1
        for letter in ran_dict.keys():
            if letter in mag_dict:
                if ran_dict[letter] > mag_dict[letter]:
                    return False
            else:
                return False
        return True


print(Solution().canConstruct(example1_arg1, example1_arg2) == example1_out)
print(Solution().canConstruct(example2_arg1, example2_arg2) == example2_out)
print(Solution().canConstruct(example3_arg1, example3_arg2) == example3_out)
