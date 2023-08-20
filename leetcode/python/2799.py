# 2799. Count Complete Subarrays in an Array

from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        distinct = len(set(nums))
        l, r = 0, 0
        subarrays = 0
        window = {}
        while r < n:
            if nums[r] not in window:
                window[nums[r]] = 0
            window[nums[r]] += 1
            while len(window) == distinct:
                subarrays += n - r
                window[nums[l]] -= 1
                if window[nums[l]] == 0:
                    del window[nums[l]]
                l += 1
            r += 1
        return subarrays
