# 2829. Determine the Minimum Sum of a k-avoiding Array

example1_arg1 = 5
example1_arg2 = 4
example1_out = 18

example2_arg1 = 2
example2_arg2 = 6
example2_out = 3


class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        avoiding_array = [1]
        num = 2
        while len(avoiding_array) < n:
            can_add = True
            for i in avoiding_array:
                if num + i == k:
                    can_add = False
                    break
            if can_add:
                avoiding_array.append(num)
            num += 1
        return sum(avoiding_array)


print(Solution().minimumSum(example1_arg1, example1_arg2) == example1_out)
print(Solution().minimumSum(example2_arg1, example2_arg2) == example2_out)
