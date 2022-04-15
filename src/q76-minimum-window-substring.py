#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ''
        result = ''
        remain = len(t)
        counter = Counter(t)
        start = 0
        for end, c in enumerate(s):
            if counter[c] > 0:
                remain -= 1
            counter[c] -= 1
            while start < end and counter[s[start]] < 0:
                counter[s[start]] += 1
                start += 1
            if remain == 0 and (not result or end - start + 1 < len(result)):
                result = s[start: end + 1]
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
