#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
from typing import List
from collections import defaultdict

# @lc code=start


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = defaultdict(list)
        dp[0].append([])
        for i in range(len(s)):
            for j in range(i + 1):
                sub = s[j:i+1]
                if sub == sub[::-1]:
                    dp[i+1].extend(perm + [sub] for perm in dp[j])
        return dp[len(s)]


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
