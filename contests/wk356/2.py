from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        distinct = len(set(nums))
        lt, rt = 0, 0
        subarrays = 0
        window = {}
        while rt < n:
            if nums[rt] not in window:
                window[nums[rt]] = 0
            window[nums[rt]] += 1
            while len(window) == distinct:
                subarrays += n - rt
                window[nums[lt]] -= 1
                if window[nums[lt]] == 0:
                    del window[nums[lt]]
                lt += 1
            rt += 1
        return subarrays
