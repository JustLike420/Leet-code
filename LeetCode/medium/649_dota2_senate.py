# https://leetcode.com/problems/dota2-senate/
from collections import deque

import pytest as pytest


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()
        for i, sen in enumerate(senate):
            radiant.append(i) if sen == 'R' else dire.append(i)
        while dire and radiant:
            radiant_i = radiant.popleft()
            dire_i = dire.popleft()
            if radiant_i < dire_i:
                radiant.append(radiant_i + n)
            else:
                dire.append(dire_i + n)
        if len(radiant) == 0:
            return 'Dire'
        else:
            return 'Radiant'


solution = Solution()


@pytest.mark.parametrize("s, expected", [
    ('RD', 'Radiant'),
    ('RDD', 'Dire')
])
def test_two_sum(s: str, expected: str):
    assert solution.predictPartyVictory(s) == expected
