# 15. 3Sum

from typing import List

example1_arg1 = [-1, 0, 1, 2, -1, -4]
example1_out = [[-1, -1, 2], [-1, 0, 1]]

example2_arg1 = [0, 1, 1]
example2_out = []

example3_arg1 = [0, 0, 0]
example3_out = [[0, 0, 0]]


class Solution:
    def threeSumV1(self, prices: List[int]) -> int:
        trips = []
        for a, i in enumerate(prices):
            hash = {}
            for b, j in enumerate(prices[a + 1 :]):
                global_idx = b + a + 1
                rem = -(j + i)
                if rem in hash:
                    if a != global_idx and a != hash[rem] and global_idx != hash[rem]:
                        temp_list = [i, j, rem]
                        temp_list.sort()
                        if temp_list not in trips:
                            trips.append(temp_list)
                else:
                    hash[j] = global_idx
        return trips

    def threeSum(self, prices: List[int]) -> int:
        trips = []
        prices.sort()
        for a, i in enumerate(prices):
            if a > 0 and i == prices[a - 1]:
                continue
            l, r = a + 1, len(prices) - 1

            while l < r:
                three_sum = i + prices[l] + prices[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    trips.append([i, prices[l], prices[r]])
                    l += 1
                    while prices[l] == prices[l - 1] and l < r:
                        l += 1
        return trips


print(Solution().threeSumV1(example1_arg1) == example1_out)
print(Solution().threeSumV1(example2_arg1) == example2_out)
print(Solution().threeSumV1(example3_arg1) == example3_out)
