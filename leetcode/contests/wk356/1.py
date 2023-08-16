from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int],
                                      target: int) -> int:
        keeners = 0
        for emp in hours:
            if emp >= target:
                keeners += 1
        return keeners
