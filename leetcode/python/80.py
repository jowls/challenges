# 80. Remove Duplicates from Sorted Array II

from typing import List

example1_arg1 = [1, 1, 1, 2, 2, 3]
example1_out1 = 5
example1_out2 = [1, 1, 2, 2, 3]

example2_arg1 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
example2_out1 = 7
example2_out2 = [0, 0, 1, 1, 2, 3, 3]


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_val = None
        current_seen = 0
        k = 0
        for i in nums:
            if i != current_val:
                current_val = i
                current_seen = 1
                nums[k] = i
                k += 1
            else:
                current_seen += 1
                if current_seen < 3:
                    nums[k] = i
                    k += 1
        return k


print(Solution().removeDuplicates(example1_arg1) == example1_out1)
print(Solution().removeDuplicates(example2_arg1) == example2_out1)
