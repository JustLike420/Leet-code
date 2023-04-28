# https://leetcode.com/problems/two-sum/
from typing import List

import pytest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i
        for i, num in enumerate(nums):
            if num in nums_map:
                dif = target - num
                if dif in nums_map.keys() and i != nums_map[dif]:
                    return [i, nums_map[dif]]
        return []


s = Solution()


@pytest.mark.parametrize("nums, target, expected", [
    ((3, 3), 6, [0, 1]),
    ([0, 1, 2, 3, 4], 7, [3, 4]),
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
])
def test_two_sum(nums, target, expected):
    assert s.twoSum(nums, target) == expected
