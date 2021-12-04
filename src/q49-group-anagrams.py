#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from typing import List
from collections import Counter, defaultdict

# @lc code=start


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        it = iter(strs)
        result = [[next(it)]]
        counters = defaultdict(list)
        counters[len(result[0][0])].append((0, Counter(result[0][0])))
        for s in it:
            counter = Counter(s)
            matched = False
            for i, c in counters[len(s)]:
                if counter == c:
                    result[i].append(s)
                    matched = True
                    break
            if not matched:
                counters[len(s)].append((len(result), counter))
                result.append([s])
        return result

# @lc code=end


solve = Solution().groupAnagrams


def test_default():
    assert solve(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']) == [
        ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert solve(['stop', 'pots', 'reed', '', 'tops', 'deer', 'opts', '']) == [
        ['stop', 'pots', 'tops', 'opts'], ['reed', 'deer'], ['', '']]


def test_corner_cases():
    assert solve(['']) == [['']]
    assert solve(['a']) == [['a']]
    assert solve(['', 'b']) == [[''], ['b']]
