# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
from typing import List
from itertools import product
import pytest as pytest


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        buttons = [
            None,
            None,
            'abc',
            'def',
            'ghi',
            'jkl',
            'mno',
            'pqrs',
            'tuv',
            'wxyz',

        ]
        buff = list(buttons[int(digit)] for digit in digits)
        answer = [''.join(button) for button in product(*buff)]
        return answer


solution = Solution()


@pytest.mark.parametrize("digits, expected", [
    ('23', ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ('', []),
    ('2', ["a", "b", "c"])
])
def test_two_sum(digits: str, expected: List[str]):
    assert solution.letterCombinations(digits) == expected
