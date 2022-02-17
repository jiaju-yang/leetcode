#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#
from typing import List
from collections import Counter

# @lc code=start


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        total = Counter(s)
        so_far = set()
        ret = []
        last_i = 0
        for i, c in enumerate(s):
            total[c] -= 1
            so_far.add(c)
            if total[c] == 0:
                if self.are_all_zero(so_far, total):
                    ret.append(i+1 - last_i)
                    last_i = i+1
                    so_far = set()
        return ret

    def are_all_zero(self, chars, counter):
        for c in chars:
            if counter[c] != 0:
                return False
        return True


# @lc code=end
solve = Solution().partitionLabels


def test_default():
    assert solve('ababcbacadefegdehijhklij') == [9, 7, 8]
    assert solve('eccbbbbdec') == [10]


def test_corner_cases():
    assert solve('a') == [1]
    assert solve('aa') == [2]
    assert solve('ab') == [1, 1]
