#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ''
        remain = len(t)
        counter = Counter(t)
        start = 0
        for end, c in enumerate(s):
            if c in counter:
                if counter[c] > 0:
                    remain -= 1
                counter[c] -= 1
                if remain == 0:
                    while True:
                        if s[start] in counter:
                            if counter[s[start]] >= 0:
                                break
                            else:
                                counter[s[start]] += 1
                                start += 1
                        else:
                            start += 1
                    if not result or len(result) > len(s[start:end+1]):
                        result = s[start:end+1]
        return result


# @lc code=end
solve = Solution().minWindow


def test_default():
    assert solve('ADOBECODEBANC', 'ABC') == 'BANC'


def test_failure_cases():
    assert solve('a', '') == ''
    assert solve('', 'a') == ''
    assert solve('a', 'aa') == ''
    assert solve('', '') == ''


def test_corner_cases():
    assert solve('a', 'a') == 'a'
    assert solve('aa', 'a') == 'a'
    assert solve('aa', 'aa') == 'aa'
