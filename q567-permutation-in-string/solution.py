#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1:
            return True
        target_match = len(s1)
        counter = Counter(s1)
        start = 0
        matched = 0
        curr_counter = dict(counter)
        for end, char in enumerate(s2):
            if end - start + 1 > target_match:
                curr_counter[s2[start]] += 1
                start += 1
                matched -= 1
            if char in counter:
                curr_counter[char] -= 1
                matched += 1
                if curr_counter[char] < 0:
                    while True:
                        curr_counter[s2[start]] += 1
                        matched -= 1
                        start += 1
                        if s2[start-1] == char:
                            break
                if matched == target_match:
                    return True
            else:
                start = end+1
                matched = 0
                curr_counter = dict(counter)
        return False


# @lc code=end
