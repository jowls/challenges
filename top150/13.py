# 13. Roman to Integer
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C,
# D and M. Given a roman numeral, convert it to an integer.

import re

example1_arg1 = "III"
example1_out = 3

example2_arg1 = "LVIII"
example2_out = 58

example3_arg1 = "MCMXCIV"
example3_out = 1994


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        s, count = re.subn(r'IV', '', s)
        result += count * 4
        s, count = re.subn(r'IX', '', s)
        result += count * 9
        s, count = re.subn(r'XL', '', s)
        result += count * 40
        s, count = re.subn(r'XC', '', s)
        result += count * 90
        s, count = re.subn(r'CD', '', s)
        result += count * 400
        s, count = re.subn(r'CM', '', s)
        result += count * 900

        for letter in s:
            if letter == 'I':
                result += 1
            elif letter == 'V':
                result += 5
            elif letter == 'X':
                result += 10
            elif letter == 'L':
                result += 50
            elif letter == 'C':
                result += 100
            elif letter == 'D':
                result += 500
            elif letter == 'M':
                result += 1000
        return result


print(Solution().romanToInt(example1_arg1) == example1_out)
print(Solution().romanToInt(example2_arg1) == example2_out)
print(Solution().romanToInt(example3_arg1) == example3_out)
