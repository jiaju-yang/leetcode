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
        remain_basket = 2
        start = 0
        max_amount = 0
        for end, fruit_type in enumerate(tree):
            if remain_basket > 0:
                baskets[fruit_type] += 1
                remain_basket = 2 - len(baskets)
                max_amount = max(sum(baskets.values()), max_amount)
            else:
                if fruit_type in baskets:
                    baskets[fruit_type] += 1
                    max_amount = max(sum(baskets.values()), max_amount)
                else:
                    while start < end:
                        baskets[tree[start]] -= 1
                        start += 1
                        if baskets[tree[start-1]] == 0:
                            del baskets[tree[start-1]]
                            break
                    baskets[fruit_type] += 1
                    max_amount = max(sum(baskets.values()), max_amount)
        return max_amount

# @lc code=end
