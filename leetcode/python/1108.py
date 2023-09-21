# 1108. Defanging an IP Address

import re


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return re.sub("\.", "[.]", address)


def test():
    solver = Solution()

    assert solver.defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1"
    assert solver.defangIPaddr("255.100.50.0") == "255[.]100[.]50[.]0"

    print("All tests passed!")
