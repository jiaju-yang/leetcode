#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
from collections import defaultdict

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        max_length = 0
        left = -1
        for right, c in enumerate(s):
            counter[c] += 1
            while counter[c] > 1:
                left += 1
                counter[s[left]] -= 1
            max_length = max(max_length, right - left)
        return max_length


# @lc code=end
solve = Solution().lengthOfLongestSubstring


def test_default():
    assert solve('abcabcbb') == 3
    assert solve('pwwkew') == 3


def test_corner_cases():
    assert solve('bbbbb') == 1
    assert solve('') == 0
