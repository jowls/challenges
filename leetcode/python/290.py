# 290. Word Pattern

from typing import List


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letter_word = {}
        word_letter = {}
        s_split = s.split()
        if len(pattern) != len(s_split):
            return False

        for letter, word in zip(pattern, s_split):
            if word in word_letter and letter in letter_word:
                if word != letter_word[letter] or letter != word_letter[word]:
                    return False
            elif word in word_letter or letter in letter_word:
                return False
            else:
                word_letter[word] = letter
                letter_word[letter] = word

        return True


def test():
    solver = Solution()

    assert solver.wordPattern("abba", "dog cat cat dog") == True
    assert solver.wordPattern("abba", "dog cat cat fish") == False
    assert solver.wordPattern("aaaa", "dog cat cat dog") == False

    print("All tests passed!")
