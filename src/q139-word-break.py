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
        max_word_len = len(max(wordDict, key=len))
        last_true = 0
        for i in range(1, len(s) + 1):
            if i > last_true + max_word_len:
                break
            for word in wordDict:
                if i - len(word) >= 0 and dp[i-len(word)]:
                    sub = s[i-len(word):i]
                    if sub == word:
                        dp[i] = True
                        last_true = i
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
