# 3. Longest Substring Without Repeating Characters

from collections import defaultdict
from typing import List


class Solution:
    # O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_freq = defaultdict(int)
        n = len(s)

        max_length = 0
        window_size = 0

        i = 0
        while i < n:
            if char_freq[s[i]] > 0:
                # remove letter from left side of window and shrink the window size
                char_freq[s[i - window_size]] -= 1
                window_size -= 1
            else:
                char_freq[s[i]] = 1
                i += 1
                window_size += 1
                max_length = max(window_size, max_length)

        return max_length


def test():
    solver = Solution()

    assert solver.lengthOfLongestSubstring("abcabcbb") == 3
    assert solver.lengthOfLongestSubstring("bbbbb") == 1
    assert solver.lengthOfLongestSubstring("pwwkew") == 3

    print("All tests passed!")
