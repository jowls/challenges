# 1832. Check if the Sentence Is Pangram


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set()
        for letter in sentence:
            if letter.isalpha():
                if letter.lower() not in alphabet:
                    alphabet.add(letter.lower())
        if len(alphabet) == 26:
            return True
        else:
            return False
