#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from typing import List
from collections import Counter, defaultdict

# @lc code=start


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = defaultdict(list)
        for s in strs:
            sorted_strs[tuple(sorted(s))].append(s)
        return list(sorted_strs.values())

# @lc code=end


solve = Solution().groupAnagrams


def test_default():
    assert solve(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']) == [
        ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert solve(['stop', 'pots', 'reed', '', 'tops', 'deer', 'opts', '']) == [
        ['stop', 'pots', 'tops', 'opts'], ['reed', 'deer'], ['', '']]


def test_corner_cases():
    assert solve(['']) == [['']]
    assert solve(['a']) == [['a']]
    assert solve(['', 'b']) == [[''], ['b']]
