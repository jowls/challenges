# 977. Squares of a Sorted Array

from typing import List

example1_arg1 = [-4, -1, 0, 3, 10]
example1_out = [0, 1, 9, 16, 100]

example2_arg1 = [-7, -3, 2, 3, 11]
example2_out = [4, 9, 9, 49, 121]


class Solution:
    def sortedSquaresV1(self, prices: List[int]) -> int:
        answer = []
        for i in prices:
            answer.append(i * i)
        # O(n log n)
        answer.sort()
        return answer

    # O(n)
    def sortedSquares(self, prices: List[int]) -> int:
        len_prices = len(prices)
        l = 0
        r = i = len_prices - 1
        answer = [0] * len_prices

        while l <= r:
            l_sqr = prices[l] ** 2
            r_sqr = prices[r] ** 2

            if l_sqr > r_sqr:
                answer[i] = l_sqr
                l += 1
            else:
                answer[i] = r_sqr
                r -= 1
            i -= 1
        return answer


print(Solution().sortedSquares(example1_arg1) == example1_out)
print(Solution().sortedSquares(example2_arg1) == example2_out)
