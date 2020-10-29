#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import Counter


class DPSolution:
    def minWindow(self, s: str, t: str) -> str:
        shortest_start = shortest_length = 0
        start = None
        need = Counter(t)
        uncovered = len(t)
        seen = {c: [] for c in t}
        for i, c in enumerate(s):
            if c in need:
                seen[c].append(i)
                if len(seen[c]) > need[c]:
                    maybe_start = seen[c].pop(0)
                    if start == maybe_start and uncovered == 0:
                        start = min(indexes[0] for indexes in seen.values())
                else:
                    uncovered -= 1
                if uncovered == 0:
                    if start is None:
                        start = min(indexes[0] for indexes in seen.values())
                    current_length = i - start + 1
                    if shortest_length == 0 or current_length < shortest_length:
                        shortest_start, shortest_length = start, current_length
        return s[shortest_start: shortest_start + shortest_length]


Solution = DPSolution
# @lc code=end
