# https://leetcode.com/problems/longest-substring-without-repeating-characters/
import pytest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        out = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in out:
                out.remove(s[l])
                l += 1
            out.add(s[r])
            res = max(res, r - l + 1)
        return res


solution = Solution()


@pytest.mark.parametrize("s, expected", [
    ('abcabcbb', 3),
    ('bbbbb', 1),
    ('pwwkew', 3),
    (' ', 1),
    ('', 0),
    ('dvdf', 3)
])
def test_two_sum(s: str, expected: int):
    assert solution.lengthOfLongestSubstring(s) == expected
