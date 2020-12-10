#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
from typing import List
from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_length = len(words[0])
        total_match_length = word_length * len(words)
        counter = Counter(words)
        result = []
        for i in range(word_length):
            for start in range(i, len(s)-total_match_length + 1, word_length):
                seen = dict(counter)
                matched = 0
                for j in range(len(words)):
                    curr_word = s[start+word_length*j:start+word_length*(j+1)]
                    if curr_word in counter:
                        seen[curr_word] -= 1
                        matched += 1
                        if seen[curr_word] < 0:
                            break
                        if matched == len(words):
                            result.append(start)
                    else:
                        break
        return result
# @lc code=end
