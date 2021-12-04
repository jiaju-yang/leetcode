#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from typing import List
from collections import Counter

# @lc code=start


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        it = iter(strs)
        result = [[next(it)]]
        counters = [Counter(result[0][0])]
        for s in it:
            counter = Counter(s)
            matched = False
            for i, c in enumerate(counters):
                if counter == c:
                    result[i].append(s)
                    matched = True
                    break
            if not matched:
                counters.append(counter)
                result.append([s])
        return result

# @lc code=end


solve = Solution().groupAnagrams


def test_default():
    assert solve(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']) == [
        ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


def test_corner_cases():
    assert solve(['']) == [['']]
    assert solve(['a']) == [['a']]
