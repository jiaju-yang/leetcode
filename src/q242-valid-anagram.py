#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
from typing import Counter

# @lc code=start


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# @lc code=end
solve = Solution().isAnagram


def test_default():
    assert solve('anagram', 'nagaram')
    assert not solve('rat', 'car')


def test_corner_cases():
    assert solve('a', 'a')
    assert not solve('a', 'b')
    assert solve('ab', 'ba')
    assert not solve('a', 'ba')
