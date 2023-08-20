# 392. Is Subsequence

example1_arg1 = "abc"
example1_arg2 = "ahbgdc"
example1_out = True

example2_arg1 = "axc"
example2_arg2 = "ahbgdc"
example2_out = False


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        s_idx = 0
        for i in t:
            if s[s_idx] == i:
                s_idx += 1
                if s_idx == len(s):
                    return True
        return False


print(Solution().isSubsequence(example1_arg1, example1_arg2) == example1_out)
print(Solution().isSubsequence(example2_arg1, example2_arg2) == example2_out)
