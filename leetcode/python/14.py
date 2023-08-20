# 14. Longest Common Prefix
from typing import List

example1_arg1 = ["flower", "flow", "flight"]
example1_out = "fl"

example2_arg1 = ["dog", "racecar", "car"]
example2_out = ""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_idx = 0
        lens = []
        for s in strs:
            lens.append(len(s))
        for i in range(0, min(lens)):
            test = strs[0][i]
            for s in strs:
                if s[i] != test:
                    return strs[0][0:prefix_idx]
            prefix_idx += 1
        return strs[0][0:prefix_idx]


print(Solution().longestCommonPrefix(example1_arg1) == example1_out)
print(Solution().longestCommonPrefix(example2_arg1) == example2_out)
