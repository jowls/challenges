# 202. Happy Number

example1_arg1 = 19
example1_out = True

example2_arg1 = 2
example2_out = False

example3_arg1 = 1
example3_out = True


class Solution:
    def isHappyV1(self, n: int) -> bool:
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

    def sumSquares(self, n: int) -> int:
        str_n = str(n)
        sum_squares = 0
        for letter in str_n:
            sum_squares += int(letter) ** 2
        return sum_squares

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        s = self.sumSquares(n)
        f = self.sumSquares(self.sumSquares(n))

        while s != f:
            s = self.sumSquares(s)
            f = self.sumSquares(self.sumSquares(f))
            if f == 1:
                return True

        return False


print(Solution().isHappy(example1_arg1) == example1_out)
print(Solution().isHappy(example2_arg1) == example2_out)
print(Solution().isHappy(example3_arg1) == example3_out)
