#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
from collections import defaultdict

# @lc code=start


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        left, max_count, right = -1, 0, 0
        for right, c in enumerate(s):
            counter[c] += 1
            max_count = max(max_count, counter[c])
            if right - left - max_count > k:
                left += 1
                counter[s[left]] -= 1
        return right - left


# @lc code=end
solve = Solution().characterReplacement


def test_default():
    assert solve('ABAB', 2) == 4
    assert solve('AABABBA', 1) == 4


def test_corner_cases():
    assert solve('a', 0) == 1
    assert solve('aa', 0) == 2
    assert solve('aa', 1) == 2
