#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
from typing import List

# @lc code=start


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry, i = True, len(digits) - 1
        while i >= 0:
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
                carry = True
                i -= 1
            else:
                break
        if i < 0 and carry:
            return [1] + digits
        return digits


# @lc code=end
solve = Solution().plusOne


def test_default():
    assert solve([1, 2, 3]) == [1, 2, 4]
    assert solve([4, 3, 2, 1]) == [4, 3, 2, 2]


def test_corner_cases():
    assert solve([9]) == [1, 0]
    assert solve([1, 9]) == [2, 0]
    assert solve([0]) == [1]
    assert solve([1]) == [2]
    assert solve([9, 9]) == [1, 0, 0]
