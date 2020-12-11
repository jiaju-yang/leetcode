#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
from typing import List
from collections import Counter, defaultdict


class BruteForceSolution:
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


class DPSolution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []
        counter = Counter(words)
        target_match = len(words)
        result = []
        word_length = len(words[0])
        for i in range(word_length):
            positions = defaultdict(list)
            matched = 0
            remain = dict(counter)
            start = i
            for j in range(i, len(s), word_length):
                curr_word = s[j:j+word_length]
                if curr_word in counter:
                    positions[curr_word].append(j)
                    matched += 1
                    remain[curr_word] -= 1
                    if remain[curr_word] < 0:
                        new_start = positions[curr_word][0] + word_length
                        while start != new_start:
                            word = s[start:start+word_length]
                            positions[word].pop(0)
                            matched -= 1
                            remain[word] += 1
                            start += word_length
                    if matched == target_match:
                        result.append(start)
                        first_word = s[start:start+word_length]
                        remain[first_word] += 1
                        start += word_length
                        matched -= 1
                        positions[first_word].pop(0)
                else:
                    positions = defaultdict(list)
                    matched = 0
                    remain = dict(counter)
                    start = j + word_length
        return result


Solution = DPSolution
# @lc code=end
