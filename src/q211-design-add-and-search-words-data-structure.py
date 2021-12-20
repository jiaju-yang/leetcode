#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#
from collections import defaultdict

# @lc code=start


class TrieNode:
    def __init__(self) -> None:
        self.leaves = defaultdict(TrieNode)
        self.exist = False

    def __getitem__(self, key):
        return self.leaves[key]

    def __iter__(self):
        return iter(self.leaves.values())


class WordDictionary:
    def __init__(self):
        self._data = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self._data
        for c in word:
            cur = cur[c]
        cur.exist = True

    def search(self, word: str) -> bool:
        curs = [self._data]
        for c in word:
            if c == '.':
                curs = [leave for cur in curs
                        for leave in cur]
            else:
                curs = [cur[c] for cur in curs]
        return any(cur.exist for cur in curs)

# @lc code=end


def test_default():
    dictionary = WordDictionary()
    assert not dictionary.search('apple')
    dictionary.addWord('bad')
    dictionary.addWord('dad')
    dictionary.addWord('mad')
    assert not dictionary.search('pad')
    assert dictionary.search('bad')
    assert dictionary.search('.ad')
    assert dictionary.search('b..')
