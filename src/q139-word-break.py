#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
from typing import List
# @lc code=start


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        wordDict = set(wordDict)
        max_word_length = max(len(word) for word in wordDict)
        for i in range(len(s)):
            for j in range(max(0, i - max_word_length+1), i+1):
                if dp[j] and s[j:i+1] in wordDict:
                    dp[i+1] = True
                    break
        return dp[-1]
# @lc code=end


solve = Solution().wordBreak


def test_default():
    assert solve('leetcode', ['leet', 'code'])
    assert solve('applepenapple', ['apple', 'pen'])
    assert not solve('catsandog', ['cats', 'dog', 'sand', 'and', 'cat'])


def test_corner_cases():
    assert solve('a', ['a'])
    assert solve('aa', ['a'])
    assert not solve('a', ['b'])
    assert solve('a', ['a', 'b'])
