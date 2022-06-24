#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
from functools import cache
from typing import List
from collections import defaultdict

# @lc code=start


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = defaultdict(list)
        dp[0].append([])
        for i in range(len(s)):
            for j in range(i + 1):
                if self.is_palindrome(j, i, s):
                    dp[i+1].extend(perm + [s[j:i+1]] for perm in dp[j])
        return dp[len(s)]

    @cache
    def is_palindrome(self, i, j, s):
        if j <= i:
            return True
        if s[i] == s[j] and self.is_palindrome(i + 1, j - 1, s):
            return True
        return False


# @lc code=end

solve = Solution().partition


def test_default():
    assert solve('aab') == [['aa', 'b'], ['a', 'a', 'b']]
    assert solve('aaba') == [['a', 'aba'], [
        'aa', 'b', 'a'], ['a', 'a', 'b', 'a']]


def test_corner_cases():
    assert solve('a') == [['a']]
    assert solve('ab') == [['a', 'b']]
    assert solve('aa') == [['aa'], ['a', 'a']]
