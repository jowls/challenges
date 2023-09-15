# 13. Roman to Integer
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C,
# D and M. Given a roman numeral, convert it to an integer.

import re


class Solution:
    # O(n), but O(1) since set of roman numerals is finite
    def romanToInt(self, s: str) -> int:
        lookup = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

        result = 0
        for i in range(len(s)):
            # check if subtraction
            if i < len(s) - 1 and lookup[s[i]] < lookup[s[i + 1]]:
                result -= lookup[s[i]]
            # otherwise simple add
            else:
                result += lookup[s[i]]
        return result

    # O(n), but O(1) since set of roman numerals is finite
    def romanToIntV1(self, s: str) -> int:
        result = 0
        s, count = re.subn(r"IV", "", s)
        result += count * 4
        s, count = re.subn(r"IX", "", s)
        result += count * 9
        s, count = re.subn(r"XL", "", s)
        result += count * 40
        s, count = re.subn(r"XC", "", s)
        result += count * 90
        s, count = re.subn(r"CD", "", s)
        result += count * 400
        s, count = re.subn(r"CM", "", s)
        result += count * 900

        for letter in s:
            if letter == "I":
                result += 1
            elif letter == "V":
                result += 5
            elif letter == "X":
                result += 10
            elif letter == "L":
                result += 50
            elif letter == "C":
                result += 100
            elif letter == "D":
                result += 500
            elif letter == "M":
                result += 1000
        return result


def test():
    solver = Solution()
    assert solver.romanToInt("III") == 3
    assert solver.romanToInt("LVIII") == 58
    assert solver.romanToInt("MCMXCIV") == 1994
    print("All tests passed!")
