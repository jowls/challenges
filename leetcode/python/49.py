# 49. Group Anagrams

from typing import List
from collections import defaultdict


class Solution:
    # O(nk): n is len(strs), and k is max len of a string in strs
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_alpha_tuple(s: str):
            alpha = [0] * 26
            for letter in s:
                alpha[ord(letter) - ord("a")] += 1

            return tuple(alpha)

        map = defaultdict(list)

        for s in strs:
            map[get_alpha_tuple(s)].append(s)

        return map.values()


def test():
    solver = Solution()

    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    out1 = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert sorted(
        [sorted(sublist) for sublist in solver.groupAnagrams(strs1)]
    ) == sorted([sorted(sublist) for sublist in out1])

    strs2 = [""]
    out2 = [[""]]
    assert sorted(
        [sorted(sublist) for sublist in solver.groupAnagrams(strs2)]
    ) == sorted([sorted(sublist) for sublist in out2])

    strs3 = ["a"]
    out3 = [["a"]]
    assert sorted(
        [sorted(sublist) for sublist in solver.groupAnagrams(strs3)]
    ) == sorted([sorted(sublist) for sublist in out3])

    print("All tests passed!")
