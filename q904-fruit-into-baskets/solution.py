#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        baskets = defaultdict(int)
        start = 0
        max_amount = 0
        for end, fruit_type in enumerate(tree):
            baskets[fruit_type] += 1
            while len(baskets) > 2:
                baskets[tree[start]] -= 1
                if baskets[tree[start]] == 0:
                    del baskets[tree[start]]
                start += 1
            max_amount = max(max_amount, end - start + 1)
        return max_amount

# @lc code=end
