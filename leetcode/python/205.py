# 205. Isomorphic Strings

example1_arg1 = "egg"
example1_arg2 = "add"
example1_out = True

example2_arg1 = "foo"
example2_arg2 = "bar"
example2_out = False

example3_arg1 = "paper"
example3_arg2 = "title"
example3_out = True


class Solution(object):
    def isIsomorphic(self, s, t):
        list1, list2 = [], []
        for idx in s:
            list1.append(s.index(idx))
        for idx in t:
            list2.append(t.index(idx))
        if list1 == list2:
            return True
        return False


print(Solution().isIsomorphic(example1_arg1, example1_arg2) == example1_out)
print(Solution().isIsomorphic(example2_arg1, example2_arg2) == example2_out)
print(Solution().isIsomorphic(example3_arg1, example3_arg2) == example3_out)
