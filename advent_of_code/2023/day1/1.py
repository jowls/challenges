from collections import defaultdict

NUMS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
IN_FILE_PATH = "advent_of_code/2023/day1/1.txt"
IN_FILE_EX1A = "advent_of_code/2023/day1/ex_1a.txt"
IN_FILE_EX1B = "advent_of_code/2023/day1/ex_1b.txt"


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False
        self.endval = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_num(self, num_word: str, endval: str) -> None:
        """Add a given num_word to the Trie

        Args:
            num_word: spelled out number to add
        """

        prev = self.root
        for c in num_word:
            prev = prev.children[c]
        prev.end = True
        prev.endval = endval

    def search_num(self, num_word: str) -> tuple[bool, str]:
        """Search for a given num_word within the Trie

        Args:
            num_word: spelled out number to seach for

        Returns:
            (bool to indicate whether num_word was found, the word value if found otherwise an empty string)
        """
        prev = self.root
        for c in num_word:
            if prev.end or c.isnumeric():
                break
            if c not in prev.children:
                return (False, "")
            prev = prev.children[c]

        return (True, prev.endval) if prev.end else (False, "")


def day_1a(infile):
    with open(infile, "r") as file:
        lines = file.readlines()

    cal_val_sum = 0
    for line in lines:
        amended_cal_val = line.strip()
        n = len(amended_cal_val)
        L = R = ""
        i = 0
        while not L or not R:
            if i > n - 1:
                break
            if not L:
                if amended_cal_val[i].isnumeric():
                    L = amended_cal_val[i]
            if not R:
                if amended_cal_val[~i].isnumeric():
                    R = amended_cal_val[~i]
            i += 1
        cal_val = int(L + R) if L and R else 0
        cal_val_sum += cal_val

    return cal_val_sum


def day_1b(infile):
    nums = NUMS
    trie = Trie()
    for i, num in enumerate(nums, 1):
        trie.add_num(num, str(i))

    with open(infile, "r") as file:
        lines = file.readlines()

    cal_val_sum = 0
    for line in lines:
        amended_cal_val = line.strip()
        n = len(amended_cal_val)
        L = R = ""
        i = 0
        while i < n:
            current_char = amended_cal_val[i]
            if current_char.isnumeric():
                R = current_char
                L = current_char if not L else L
            else:
                found, val = trie.search_num(amended_cal_val[i:])
                if found:
                    R = val
                    L = val if not L else L
            i += 1
        # print(int(L + R))
        cal_val_sum += int(L + R)

    return cal_val_sum


# print(day_1a(IN_FILE_PATH))
# print(day_1b(IN_FILE_PATH))
assert day_1a(IN_FILE_PATH) == 55172
assert day_1b(IN_FILE_PATH) == 54925
assert day_1a(IN_FILE_EX1A) == 142
assert day_1b(IN_FILE_EX1B) == 281
