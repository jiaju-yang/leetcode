#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def find_max_in_subset(start, target_m, target_n, curr_size):
            nonlocal max_size
            if target_m == 0 and target_n == 0 and curr_size > max_size:
                max_size = curr_size
            if target_m < 0 or target_n < 0:
                return
            if start >= len(strs):
                return
            curr_m, curr_n = self.count_01s(strs[start])
            find_max_in_subset(start + 1, target_m - curr_m,
                   target_n - curr_n, curr_size + 1)
            find_max_in_subset(start + 1, target_m, target_n, curr_size)
        max_size = 0
        find_max_in_subset(0, m, n, 0)
        return max_size

    def count_01s(self, seq):
        counter = Counter(seq)
        return (counter['0'] if '0' in counter else 0,
                counter['1'] if '1' in counter else 0)
# @lc code=end
