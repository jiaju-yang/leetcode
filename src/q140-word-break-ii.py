#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
from typing import List

# @lc code=start


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        return [' '.join(words) for words in self.break_words(s, words)]

    def break_words(self, remain, words):
        if not remain:
            return [[]]
        result = []
        for i in range(min(10, len(remain))):
            if remain[:i+1] in words:
                sub_results = self.break_words(remain[i+1:], words)
                for sub_result in sub_results:
                    result.append([remain[:i+1]] + sub_result)
        return result


# @lc code=end
solve = Solution().wordBreak


def test_default():
    assert set(solve('catsanddog', ["cat", "cats", "and", "sand", "dog"]
                     )) == set(["cats and dog", "cat sand dog"])
    assert set(solve('pineapplepenapple', ["apple", "pen", "applepen", "pine", "pineapple"]
                     )) == set(["pine apple pen apple", "pineapple pen apple", "pine applepen apple"])
    assert set(solve('catsandog', ["cats", "dog", "sand", "and", "cat"]
                     )) == set([])


def test_corner_cases():
    assert solve('a', ['a']) == ['a']
    assert solve('a', ['b']) == []
    assert solve('aa', ['a']) == ['a a']
    assert solve('ab', ['a', 'b']) == ['a b']
