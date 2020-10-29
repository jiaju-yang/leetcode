#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import defaultdict


class DPSolution:
    def minWindow(self, s: str, t: str) -> str:
        shortest_s = ''
        need = defaultdict(int)
        for c in t:
            need[c] += 1
        uncovered = len(t)
        seen = {c: [] for c in t}
        for i, c in enumerate(s):
            if c in need:
                seen[c].append(i)
                if len(seen[c]) > need[c]:
                    seen[c].pop(0)
                else:
                    uncovered -= 1
                if uncovered == 0:
                    start = min(indexes[0] for indexes in seen.values())
                    current_length = i - start + 1
                    if len(shortest_s) == 0 or current_length < len(shortest_s):
                        shortest_s = s[start:start + current_length]
        return shortest_s


Solution = DPSolution
# @lc code=end
