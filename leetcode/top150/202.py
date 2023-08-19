# 202. Happy Number

example1_arg1 = 19
example1_out = True

example2_arg1 = 2
example2_out = False


class Solution:
    def isHappy(self, n: int) -> bool:
        results = {}
        str_n = str(n)
        while True:
            sum_squares = 0
            for letter in str_n:
                sum_squares += int(letter) ** 2
            if sum_squares == 1:
                return True
            elif sum_squares in results:
                return False
            else:
                results[sum_squares] = 1
                str_n = str(sum_squares)


print(Solution().isHappy(example1_arg1) == example1_out)
print(Solution().isHappy(example2_arg1) == example2_out)
