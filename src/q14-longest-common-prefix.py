#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from typing import List

# @lc code=start


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret, i = '', 0
        while True:
            try:
                c = strs[0][i]
                if any(c != s[i] for s in strs):
                    return ret
            except IndexError:
                return ret
            ret += c
            i += 1


# @lc code=end
solve = Solution().longestCommonPrefix


def test_default():
    assert solve(['flower', 'flow', 'flight']) == 'fl'
    assert solve(['dog', 'racecar', 'car']) == ''


def test_corner_cases():
    assert solve(['']) == ''
    assert solve(['', 'a']) == ''
    assert solve(['a']) == 'a'
    assert solve(['a', 'b']) == ''
    assert solve(['a', 'a']) == 'a'
