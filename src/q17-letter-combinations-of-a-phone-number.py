#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from typing import List, Mapping

# @lc code=start


class Solution:
    mapping = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = ['']
        for digit in digits:
            result = [p+c for p in result
                      for c in self.mapping[digit]]
        return result


# @lc code=end
solve = Solution().letterCombinations


def test_default():
    assert solve('23') == ['ad', 'ae', 'af', 'bd',
                           'be', 'bf', 'cd', 'ce', 'cf']


def test_corner_cases():
    assert solve('') == []
    assert solve('2') == ['a', 'b', 'c']
