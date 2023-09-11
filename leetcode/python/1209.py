# 1209. Remove All Adjacent Duplicates in String II


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # stack of pairs representing the character and its seen count
        stack = []

        for letter in s:
            # if the letter is going to cause a repeat
            if stack and letter == stack[-1][0]:
                # increment the seen count
                stack[-1][1] += 1
                # if we hit k, pop it all
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([letter, 1])

        # construct the result string from the stack
        result = ""
        for letter_pair in stack:
            result += letter_pair[0] * letter_pair[1]

        return result


def test():
    solver = Solution()

    assert solver.removeDuplicates("abcd", 2) == "abcd"
    assert solver.removeDuplicates("deeedbbcccbdaa", 3) == "aa"
    assert solver.removeDuplicates("pbbcggttciiippooaais", 2) == "ps"
    assert (
        solver.removeDuplicates("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", 4) == "ybth"
    )

    print("All tests passed!")
