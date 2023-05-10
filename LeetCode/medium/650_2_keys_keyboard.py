# https://leetcode.com/problems/2-keys-keyboard/
import pytest as pytest


class Solution:
    def minSteps(self, n: int) -> int:
        count = 0
        d = 2
        while n > 1:
            while n % d == 0:
                n /= d
                count += d
            d += 1
        return count


solution = Solution()


@pytest.mark.parametrize("n, expected", [
    (3, 3),
    (1, 0)
])
def test_two_sum(n: int, expected: int):
    assert solution.minSteps(n) == expected
