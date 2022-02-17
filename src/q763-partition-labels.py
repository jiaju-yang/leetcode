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
        total, so_far = Counter(s), set()
        remain = last_i = 0
        ret = []
        for i, c in enumerate(s):
            if c not in so_far:
                so_far.add(c)
                remain += total[c]
            total[c] -= 1
            remain -= 1
            if remain == 0:
                ret.append(i+1 - last_i)
                last_i = i+1
                so_far = set()
        return ret


# @lc code=end
solve = Solution().partitionLabels


def test_default():
    assert solve('ababcbacadefegdehijhklij') == [9, 7, 8]
    assert solve('eccbbbbdec') == [10]


def test_corner_cases():
    assert solve('a') == [1]
    assert solve('aa') == [2]
    assert solve('ab') == [1, 1]
