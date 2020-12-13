#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, max_count, result = 0, 0, 0
        counter = defaultdict(int)
        for i, c in enumerate(s):
            counter[c] += 1
            max_count = max(max_count, counter[c])
            while i-start+1-max_count > k:
                counter[s[start]] -= 1
                max_count = max(max_count, counter[c])
                start += 1
            result = max(result, i-start+1)
        return result

# @lc code=end
