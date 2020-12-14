#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target_match = len(p)
        matched = 0
        result = []
        start = 0
        counter = Counter(p)
        curr_counter = dict(counter)
        for end, char in enumerate(s):
            if end - start + 1 > target_match:
                curr_counter[s[start]] += 1
                matched -= 1
                start += 1
            if char in counter:
                curr_counter[char] -= 1
                if curr_counter[char] < 0:
                    while True:
                        curr_counter[s[start]] += 1
                        matched -= 1
                        start += 1
                        if s[start-1] == char:
                            break
                matched += 1
                if matched == target_match:
                    result.append(start)
            else:
                start = end + 1
                matched = 0
                curr_counter = dict(counter)
        return result

# @lc code=end
