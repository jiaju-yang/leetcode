#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minimum_substring = ''
        counter = Counter(t)
        remain = len(t)
        left, right = 0, 0
        for right, char in enumerate(s):
            if char in counter:
                if counter[char] > 0:
                    remain = max(0, remain - 1)
                counter[char] -= 1
                while True:
                    if s[left] not in counter:
                        left += 1
                    else:
                        if counter[s[left]] < 0:
                            counter[s[left]] += 1
                            left += 1
                        else:
                            break
                sub = s[left:right+1]
                if remain == 0 and (minimum_substring == '' or len(minimum_substring) > len(sub)):
                    minimum_substring = sub

        return minimum_substring


# @lc code=end
