#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
import string
from typing import List

# @lc code=start


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set([beginWord])
        all_words = set(wordList)
        q = [beginWord]
        path_count = 0
        while q:
            new_q = []
            path_count += 1
            for word in q:
                if word == endWord:
                    return path_count
                valid_adjs = [adj for adj in self.adj_words(
                    word, all_words) if adj not in visited]
                visited.update(valid_adjs)
                new_q.extend(valid_adjs)
            q = new_q
        return 0

    def adj_words(self, origin, word_set):
        ret = []
        for i in range(len(origin)):
            for l in string.ascii_lowercase:
                potential = origin[:i] + l + origin[i+1:]
                if potential in word_set:
                    ret.append(potential)
        return ret


# @lc code=end
solve = Solution().ladderLength


def test_default():
    assert solve('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert solve('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]) == 0


def test_corner_cases():
    assert solve('a', 'b', ['b']) == 2
    assert solve('a', 'b', ['c']) == 0
