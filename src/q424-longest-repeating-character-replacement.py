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
        left = -1
        max_length = 0
        for right, c in enumerate(s):
            counter[c] += 1
            max_count = max(counter.values())
            if right - left - max_count > k:
                left += 1
                counter[s[left]] -= 1
            max_length = max(max_length, right - left)
        return max_length


# @lc code=end
solve = Solution().characterReplacement


def test_default():
    assert solve('ABAB', 2) == 4
    assert solve('AABABBA', 1) == 4


def test_corner_cases():
    assert solve('', 0) == 0
    assert solve('', 1) == 0
    assert solve('a', 0) == 1
    assert solve('aa', 0) == 2
    assert solve('aa', 1) == 2
