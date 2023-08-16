# 9. Palindrome Number

import math

example1_arg1 = 121
example1_out = True

example2_arg1 = -121
example2_out = False

example3_arg1 = 10
example3_out = False


class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        mid = math.floor(len(str_x) / 2)
        end = len(str_x) - 1
        for i in range(mid):
            if str_x[i] != str_x[end]:
                return False
            end -= 1
        return True


print(Solution().isPalindrome(example1_arg1) == example1_out)
print(Solution().isPalindrome(example2_arg1) == example2_out)
print(Solution().isPalindrome(example3_arg1) == example3_out)
